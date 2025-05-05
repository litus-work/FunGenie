import telebot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
from telebot.util import quick_markup
import config
from services.groq_client import chat_with_groq
from services.utils import remove_think_blocks




TOKEN = config.TELEGRAM_TOKEN
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message: Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("🎬 Фильмы"), KeyboardButton("🎵 Музыка"))
    markup.row(KeyboardButton("😂 Анекдоты"), KeyboardButton("📖 Истории"))
    markup.row(KeyboardButton("🎮 Игры"))

    bot.send_message(
        message.chat.id,
        "Привет! Я FunGenie 🤖 — твой помощник по развлечениям.\nВыбери категорию:",
        reply_markup=markup
    )
@bot.message_handler(func=lambda message: message.text == "🎬 Фильмы")
def handle_movies(message: Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("🎭 Комедия"), KeyboardButton("🔫 Боевик"))
    markup.row(KeyboardButton("👻 Ужасы"), KeyboardButton("🚀 Фантастика"))
    markup.row(KeyboardButton("💖 Мелодрама"), KeyboardButton("🎲 Случайный жанр"))
    markup.row(KeyboardButton("🔙 Назад"))

    bot.send_message(
        message.chat.id,
        "Выберите жанр фильма 🎭",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "🎭 Комедия")
def handle_comedy_genre(message: Message):
    prompt = (
        "Составь список из 5 лучших комедийных фильмов разных годов. "
        "Для каждого фильма укажи:\n"
        "1. Название (жирным)\n"
        "2. Год выпуска (в скобках)\n"
        "3. Краткое описание (1–2 предложения)\n\n"
        "Не добавляй вступление, размышления, выводы и не используй теги <think>. "
        "Выведи только финальный список фильмов, начиная с 1."
    )

    bot.send_chat_action(message.chat.id, 'typing')  # визуальный эффект

    response = chat_with_groq(prompt)
    cleaned_response = remove_think_blocks(response)

    bot.send_message(message.chat.id, cleaned_response)

bot.infinity_polling()
