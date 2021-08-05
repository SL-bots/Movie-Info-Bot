# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import json
import requests 
from .commands import *
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


API = "https://api.sumanjay.cf/watch/query="


@Client.on_message(filters.command(["info", "information"]), group=2)
async def get_command(bot, update):
    movie = requote_uri(update.text.split(" ", 1)[1])
    username = (await bot.get_me()).username
    keyboard = [
        InlineKeyboardButton(
            text="Click here",
            url=f"https://telegram.me/{username}?start={movie}"
        )
    ]
    await update.reply_text(
        text=f"**Click the button below**",
        reply_markup=InlineKeyboardMarkup([keyboard]),
        disable_web_page_preview=True,
        quote=True
    )


@Client.on_message(filters.private & filters.text & ~filters.via_bot)
async def get_movie_name(bot, update):
    if update.text.startswith("/"):
        return
    await get_movie(bot, update, update.text)


async def get_movie(bot, update, name):
    movie_name = requote_uri(name)
    movie_api = API + movie_name
    r = requests.get(movie_api)
    movies = r.json()
    keyboard = []
    number = 0
    for movie in movies:
        number += 1
        switch_text = movie_name + "+" + str(number)
        try:
            keyboard.append(
                [
                    InlineKeyboardButton(
                        text=description(movie),
                        switch_inline_query_current_chat=switch_text
                    )
                ]
            )
        except:
            pass
    keyboard.append(JOIN_BUTTONS)
    await update.reply_text(
        text="Select required option",
        reply_markup=InlineKeyboardMarkup(keyboard),
        disable_web_page_preview=True,
        quote=True
    )


def description(movie):
    set = []
    if movie['title']:
        set.append(movie['title'])
    if movie['type']:
        set.append(movie['type'].capitalize())
    if movie['release_year']:
        set.append(str(movie['release_year']))
    description = " | ".join(set)
    return description


def info(movie):
    info = f"**Title:** `{movie['title']}`\n"
    try:
        info += f"**Type:** `{movie['type'].capitalize()}`\n"
    except:
        pass
    try:
        info += f"**Release Date:** `{str(movie['release_date'])}`\n"
    except:
        pass
    try:
        info += f"**Release Year:** `{movie['release_year']}`\n"
    except:
        pass
    try:
        if movie['score']:
            scores = movie['score']
            info += "**Score:** "
            score_set = []
            for score in scores:
                score_set.append(f"{score.upper()} - `{str(scores[score])}`")
            info += " | ".join(score_set) + "\n"
    except:
        pass
    try:
        if movie['providers']:
            info += "**Providers:** "
            providers = movie['providers']
            provider_set = []
            for provider in providers:
                provider_set.append(f"[{provider.capitalize()}]({providers[provider]})")
            info += " | ".join(provider_set)
    except:
        pass
    return info


def thumb(movie):
    thumbnail = movie['movie_thumb'] if movie['movie_thumb'] else None
    return thumbnail
