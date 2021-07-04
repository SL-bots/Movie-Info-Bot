# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)


import requests
from pyrogram import Client, filters 
from pyrogram.types import *
from plugins.info import *


@Client.on_inline_query()
async def inline_info(bot, update):
    query = update.query
    movie_name = query.replace(" ", "+")
    r = requests.get(API + movie_name)
    movies = r.json()
    answers = []
    for movie in movies:
        photo = thumb(movie)
        movie_info = info(movie)
        keyboard = providers(movie) if movie['providers'] else []
        answers.append(
            InlineQueryResultArticle(
                title=movie['title'],
                thumb_url=photo,
                description=f"{movie['title']} - {movie['type']} - {movie['release_year']}",
                input_message_content=InputTextMessageContent(
                    message_text=movie_info,
                    disable_web_page_preview=True
                ),
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        )
        await bot.answer_inline_query(
            inline_query_id=update.id,
            results=answers
        )
