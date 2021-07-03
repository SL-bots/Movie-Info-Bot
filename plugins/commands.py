# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from plugins.info import *


@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    if update.text == "/start":
        await update.reply_text(f"Hi {update.from_user.mention}")
    else:
        movie = update.text.split(" ", 1)
        await get_movie(bot, update, movie)
