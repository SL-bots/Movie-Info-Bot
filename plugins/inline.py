# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)


imported
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from plugins.info import *


@Client.on_inline_query()
async def inline_info(bot, update):
        data = update.data
        number, movie_api = update.data.split("+", -1)
        r = requests.get(movie_api)
        movies = r.json()
        answers = []
        try:
            movie = movies[number-1]
            movie_info = info(movie)
        except Exception as error:
            print(error)
            
