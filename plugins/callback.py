# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from plugins.info import *


@Client.on_callback_query()
async def callback(bot, update):
    if update.data.startswith("movie+"):
        startwidth, movie, type = update.data.split("+", 2)
        await cb_edit(bot, update.message, movie, type)
