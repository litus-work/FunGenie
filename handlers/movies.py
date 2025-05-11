##handlers/movies.py
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
from services.groq_client import chat_with_groq
from services.promts import movie_promt
from handlers import menu
from funbot import bot

from services.utils import remove_think_blocks

@bot.message_handler(func=lambda message: message.text == "🎬 Фильмы")
def handle_movies(message: Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("🎭 Комедия"), KeyboardButton("🔫 Боевик"))
    markup.row(KeyboardButton("👻 Ужасы"), KeyboardButton("🚀 Фантастика"))
    markup.row(KeyboardButton("💖 Мелодрама"), KeyboardButton("🎲 Случайный жанр"))
    markup.row(KeyboardButton("📝 Ввести жанр фильма вручную"),KeyboardButton("🔙 Назад"))

    bot.send_message(
        message.chat.id,
        "Выберите жанр фильма 🎭",
        reply_markup=markup
    )


def handle_movie_genre(message: Message, genre: str):
    prompt = movie_promt(genre)
    bot.send_chat_action(message.chat.id, 'typing')
    response = chat_with_groq(prompt)
    cleaned_response = remove_think_blocks(response)
    bot.send_message(message.chat.id, cleaned_response, parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == "📝 Ввести жанр фильма вручную")
def ask_for_custom_genre(message: Message):
    bot.send_message(message.chat.id, "Введите жанр фильма, который вас интересует (например: триллер, фэнтези, драма):")
    bot.register_next_step_handler(message, process_custom_genre)

def process_custom_genre(message: Message):
    user_genre = message.text.strip().lower()
    print(f"User entered genre: {user_genre}")
    handle_movie_genre(message, user_genre)

@bot.message_handler(func=lambda message: message.text == "🎭 Комедия")
def handle_comedy(message: Message):
    handle_movie_genre(message, "комедия")


@bot.message_handler(func=lambda message: message.text == "👻 Ужасы")
def handle_horror(message: Message):
    handle_movie_genre(message, "ужасы")


@bot.message_handler(func=lambda message: message.text == "🔫 Боевик")
def handle_action(message: Message):
    handle_movie_genre(message, "боевик")


@bot.message_handler(func=lambda message: message.text == "🚀 Фантастика")
def handle_scifi(message: Message):
    handle_movie_genre(message, "фантастика")


@bot.message_handler(func=lambda message: message.text == "💖 Мелодрама")
def handle_romance(message: Message):
    handle_movie_genre(message, "мелодрама")

@bot.message_handler(func=lambda message: message.text == "🎲 Случайный жанр")
def handle_romance(message: Message):
    handle_movie_genre(message, "cлучайный")


@bot.message_handler(func=lambda message: message.text == "🔙 Назад")
def handle_back(message: Message):
    menu.start(message)

