# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from pyrogram import Client

@Client.on_callback_query()
async def callback(bot, update):
    if update.query.startswith("movie+"):
        data = update.data.split("movie+", 1)
        movie, type = data.data.split("+", 1)
        await cb_edit(bot, update.message, movie, type)
