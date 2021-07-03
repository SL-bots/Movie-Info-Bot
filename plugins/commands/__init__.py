# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from pyrogram import Client, filters


@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    if update.text == "/start":
        pass
    else:
        movie = update.text.split(" ", 1)
        await get_movie(bot, update.message, movie)
