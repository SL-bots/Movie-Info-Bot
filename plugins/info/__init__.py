# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


API = 'https://api.sumanjay.cf/watch/'


@Client.on_message(filters.command(["info", "information"]))
async def get_command(bot, update):
    movie = update.text.split(" ", 1)
    movie = name.replace(" ", "+").replace("\n", "+").lower()


@Client.on_message(filters.private & filters.text)
async def get_movie(bot, update):
    movie = update.text
    movie = name.replace(" ", "+").replace("\n", "+").lower()


def movie(name):
    response = requests.get(API + movie_name)
    movies = response.json()
    for movie in movies:
        info = info(movie)
        thumb = thumb(movie)
    return info, thumb


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
