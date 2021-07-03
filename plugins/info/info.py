# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from plugins.info import movie


@Client.on_message(filters.command(["info", "information"]))
async def get_command(bot, update):
    movie = update.text.split(" ", 1)
    info, thumb = movie(movie)

@Client.on_message(filters.private & filters.text)
async def get_movie(bot, update):
    movie = update.text
    info, thumb = movie(movie)
