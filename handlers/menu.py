##handlers/menu.py
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
from funbot import bot


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


from handlers import movies, music

@bot.message_handler(func=lambda message: message.text == "🔙 Назад")
def handle_back(message: Message):
    start(message)

