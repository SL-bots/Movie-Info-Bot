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
        description = movie['title'] if movie['title'] else None
        description += f" - {movie['type']..capitalize()}" if movie['type'] else None
        description += f" - ({str(movie['release_year'])})" if movie['release_year'] else None
        photo = thumb(movie)
        movie_info = info(movie)
        keyboard = providers(movie['providers'])
        answers.append(
            InlineQueryResultArticle(
                title=movie['title'],
                thumb_url=photo,
                description=description",
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
