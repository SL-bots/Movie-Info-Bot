# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)


import requests
from pyrogram import Client, filters 
from pyrogram.types import *
from plugins.info import *


@Client.on_inline_query()
async def inline_info(bot, update):
        query = update.query
        number, movie_name = query.split("+", -1)
        number = round(str(number) - 1)
        r = requests.get(API + movie_name)
        movies = r.json()
        movie = movies[number]
        movie_info = info(movie)
        answers = [
            InlineQueryResultArticle(
                title=movie['title'],
                description=f"{movie['title']} - {movie['type']} - {movie['year']}",
                input_message_content=InputTextMessageContent(
                    text=movie_info,
                    disable_web_page_preview=True
                )
            )
        ]
        await bot.answer_inline_query(
            inline_query_id=update.chat.id,
            results=answers
        )
