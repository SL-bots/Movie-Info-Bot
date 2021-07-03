# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


API = 'https://api.sumanjay.cf/watch/'


@Client.on_message(filters.command(["info", "information"]))
async def get_command(bot, update):
    movie = update.text.split(" ", 1).replace(" ", "+").replace("\n", "+").lower()
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


@Client.on_message(filters.private & filters.text)
async def get_movie_name(bot, update):
    await get_movie(bot, update.message, update.text)


async def get_movie(bot, update, movie):
    movie_name = movie.replace(" ", "+").replace("\n", "+").lower()
    response = requests.get(API + movie_name)
    movies = response.json()
    keyboard = []
    for i in movies:
        movie = i.replace(" ", "+").replace("\n", "+").lower()
        keyboard.append([
            InlineKeyboardButton(
                text=f"{movie['title']} - {movie['type']}",
                callback_data=f"movie+{movie['title']}+{movie['type']}"
            )
        ]
    await update.reply_text(
        text="Select required option",
        reply_markup=InlineKeyboardMarkup(keyboard),
        disable_web_page_preview=True,
        quote=True
    )


def info(movie):
    info = f"Title: {movie['title']}\n"
    info += f"Type: {movie['type']}\n"
    if movie['providers']:
        providers = movie['providers']
        info += f"Providers:"
        try:
            providers = movie['providers']
            for provider in providers:
                info += f" [{provider}]({providers[provider]})"
            info += "\n"
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
