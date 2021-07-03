# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from pyrogram import Client
from plugins.info import cb_edit


@Client.on_callback_query()
async def callback(bot, update):
    if update.data.startswith("movie+"):
        movie, type, year = update.data.split("+", 3)
        await cb_edit(bot, update.message, movie, type, year)
