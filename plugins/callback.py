# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from pyrogram import Client

@Client.on_callback_query()
async def callback(bot, update):
    if update.query.startswith("movie+"):
        movie = update.query.split("movie+", 1)
