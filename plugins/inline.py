# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)


import requests
from requests.utils import requote_uri
from pyrogram import Client, filters 
from pyrogram.types import *
from .commands import *
from .info import *


@Client.on_inline_query()
async def inline_info(bot, update):
    query = update.query
    num = None
    if "+" in query:
        movie_name, num = query.split("+", -1)
    else:
        movie_name = query
    r = requests.get(API + requote_uri(movie_name))
    movies = [r.json()[int(num) - 1]] if num else r.json()
    answers = []
    for movie in movies:
        set = []
        set.append(movie['title'] if movie['title'] else None)
        set.append(movie['type'].capitalize() if movie['type'] else None)
        set.append(str(movie['release_year'])}) if movie['release_year'] else None)
        description = " - ".join(set)
        photo = thumb(movie)
        movie_info = info(movie)
        keyboard = BUTTONS
        answers.append(
            InlineQueryResultArticle(
                title=movie['title'],
                thumb_url=photo,
                description=description,
                input_message_content=InputTextMessageContent(
                    message_text=movie_info,
                    disable_web_page_preview=True
                ),
                reply_markup=keyboard
            )
        )
    await bot.answer_inline_query(
        inline_query_id=update.id,
        results=answers
    )
