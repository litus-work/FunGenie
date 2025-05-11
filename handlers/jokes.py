#handlers/music.py

from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
from services.groq_client import chat_with_groq
from services.promts import music_prompt
from services.utils import remove_think_blocks
from funbot import bot

from handlers import menu

@bot.message_handler(func=lambda message: "Музыка" in message.text)
def handle_music(message: Message):
    print("handle_music")
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("🎸 Рок"), KeyboardButton("🎤 Поп"))
    markup.row(KeyboardButton("🎧 Электронная"), KeyboardButton("🎷 Джаз"))
    markup.row(KeyboardButton("🎹 Классика"), KeyboardButton("🎼 Саундтреки"))
    markup.row(KeyboardButton("🎶 Рэп / Хип-хоп"), KeyboardButton("🎻 Инструментал"))
    markup.row(KeyboardButton("🪗 Фолк"), KeyboardButton("🌍 World music"))
    markup.row(KeyboardButton("🔀 Случайный жанр"), KeyboardButton("🔙 Назад"))
    markup.row(KeyboardButton("📝 Ввести жанр музыки вручную"))

    bot.send_message(
        message.chat.id,
        "Выберите жанр музыки 🎵",
        reply_markup=markup
    )

def handle_music_genre(message: Message, genre: str):
    prompt = music_prompt(genre)
    bot.send_chat_action(message.chat.id, 'typing')
    response = chat_with_groq(prompt)
    cleaned_response = remove_think_blocks(response)
    bot.send_message(message.chat.id, cleaned_response, parse_mode='Markdown')



@bot.message_handler(func=lambda message: message.text == "🎸 Рок")
def handle_rock(message: Message):
    handle_music_genre(message, "рок")

@bot.message_handler(func=lambda message: message.text == "🎤 Поп")
def handle_pop(message: Message):
    handle_music_genre(message, "поп")

@bot.message_handler(func=lambda message: message.text == "🎧 Электронная")
def handle_electronic(message: Message):
    handle_music_genre(message, "электронная")

@bot.message_handler(func=lambda message: message.text == "🎷 Джаз")
def handle_jazz(message: Message):
    handle_music_genre(message, "джаз")

@bot.message_handler(func=lambda message: message.text == "🎹 Классика")
def handle_classical(message: Message):
    handle_music_genre(message, "классическая музыка")

@bot.message_handler(func=lambda message: message.text == "🎼 Саундтреки")
def handle_soundtracks(message: Message):
    handle_music_genre(message, "саундтреки")

@bot.message_handler(func=lambda message: message.text == "🎶 Рэп / Хип-хоп")
def handle_rap(message: Message):
    handle_music_genre(message, "рэп")

@bot.message_handler(func=lambda message: message.text == "🎻 Инструментал")
def handle_instrumental(message: Message):
    handle_music_genre(message, "инструментал")

@bot.message_handler(func=lambda message: message.text == "🪗 Фолк")
def handle_folk(message: Message):
    handle_music_genre(message, "фолк")

@bot.message_handler(func=lambda message: message.text == "🌍 World music")
def handle_world(message: Message):
    handle_music_genre(message, "world music")

@bot.message_handler(func=lambda message: message.text == "🔀 Случайный жанр")
def handle_world(message: Message):
    handle_music_genre(message, "случайный жанр")

@bot.message_handler(func=lambda message: message.text == "📝 Ввести жанр музыки вручную")
def ask_for_custom_genre(message: Message):
    bot.send_message(message.chat.id, "Введите жанр музыки, который вас интересует (например: роп, поп, электронная):")
    bot.register_next_step_handler(message, process_custom_genre)

def process_custom_genre(message: Message):
    user_genre = message.text.strip().lower()
    print(f"User entered genre: {user_genre}")
    handle_music_genre(message, user_genre)


@bot.message_handler(func=lambda message: message.text == "🔙 Назад")
def handle_back(message: Message):
    menu.start(message)


