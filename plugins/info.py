# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


API = 'https://api.sumanjay.cf/watch/'


@Client.on_message(filters.command(["info", "information"]))
async def get_command(bot, update):
    movie = update.text.split(" ", 1)
    movie = movie.replace(" ", "+")
    movie = movie.replace("\n", "+")
    keyboard = [
        InlineKeyboardButton(
            text="Click here",
            url=f"https://telegram.me/{username}?start={movie}"
        )
    ]
    await update.reply_text(
        text=f"Click the button below",
        reply_markup=InlineKeyboardMarkup([keyboard]),
        disable_web_page_preview=True,
        quote=True
    )


@Client.on_message(filters.private & filters.text & ~filters.command(["start"]))
async def get_movie_name(bot, update):
    await get_movie(bot, update, update.text)


async def get_movie(bot, update, movie):
    movie_name = movie.replace(" ", "+")
    movie_name = movie_name.replace("\n", "+")
    r = requests.get(API + movie_name)
    movies = r.json()
    keyboard = []
    for movie in movies:
        keyboard.append(
            [
                InlineKeyboardButton(
                    text=f"{movie['title']} - {movie['type']}",
                    switch_inline_query_current_chat=movie
                )
            ]
        )
    await update.reply_text(
        text="Select required option",
        reply_markup=InlineKeyboardMarkup(keyboard),
        disable_web_page_preview=True,
        quote=True
    )


async def cb_edit(bot, update, movie, type):
    movie_name = movie.replace("_", "+")
    r = requests.get(API + movie_name)
    movies = r.json()
    title = movie.replace("_", " ")
    type_movie = type.replace("_", " ")
    for info in movies:
        if (title in info['title'] or info['title'] in title) and (type_movie in info['type'] or info['type'] in type_movie):
            try:
                information = info(movie)
            except Exception as error:
                information = error
    await update.edit_text(
        text=information,
        disable_web_page_preview=True
    )


def info(movie):
    info = f"Title: {movie['title']}\n"
    info += f"Type: {movie['type']}\n"
    if movie['providers']:
        try:
            providers = movie['providers']
            info += f"Providers:"
            for provider in providers:
                info += f" [{provider}]({providers[provider]})"
            info += "\n"
        except:
            pass
    try:
        info += f"Release Date: {str(movie['release_date'])}\n"
    except:
        pass
    try:
        info += f"Release Year: {movie['release_year']}\n"
    except:
        pass
    try:
        if movie['score']:
            scores = movie['score']
            info += "Score:"
            for score in scores:
                info += f" {score} - {str(scores[score])}"
    except:
        pass
    return info


def thumb(movie):
    thumbnail = movie['movie_thumb']
    return thumbnail
