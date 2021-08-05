# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from plugins.info import *

START_TEXT = """
Hello {}
I am a movie information finder bot.

> `I can find information of all movies.`

Made by @FayasNoushad
"""
JOIN_BUTTONS = [InlineKeyboardButton(text='⚙ Join Updates Channel ⚙', url='https://telegram.me/FayasNoushad')]
BUTTONS = InlineKeyboardMarkup([JOIN_BUTTONS])

@Client.on_message(filters.private & filters.command(["start"]), group=-1)
async def start(bot, update):
    if update.text == "/start":
        await update.reply_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=BUTTONS,
            quote=True
        )
    else:
        movie = update.text.split(" ", 1)[1]
        await get_movie(bot, update, movie)
