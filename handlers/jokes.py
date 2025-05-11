from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
from funbot import bot
from services.groq_client import chat_with_groq
from services.utils import remove_think_blocks
from services.promts import joke_prompt
from handlers import menu

@bot.message_handler(func=lambda message: "Анекдоты" in message.text)
def handle_jokes(message: Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("👨‍⚕️ Врачи"), KeyboardButton("👮 Менты"))
    markup.row(KeyboardButton("👩‍🏫 Школа"), KeyboardButton("💼 Работа"))
    markup.row(KeyboardButton("👨‍💻 IT"), KeyboardButton("👨‍👩‍👧‍👦 Семья"))
    markup.row(KeyboardButton("🎲 Случайный"), KeyboardButton("🔙 Назад"))
    markup.row(KeyboardButton("✍️ Ввести жанр анекдота"))

    bot.send_message(message.chat.id, "Выбери жанр анекдотов 😂", reply_markup=markup)


def handle_joke_genre(message: Message, genre: str):
    prompt = joke_prompt(genre)
    bot.send_chat_action(message.chat.id, 'typing')
    response = chat_with_groq(prompt)
    cleaned = remove_think_blocks(response)
    bot.send_message(message.chat.id, cleaned, parse_mode='Markdown')

# Хендлеры жанров:

@bot.message_handler(func=lambda m: m.text == "👨‍⚕️ Врачи")
def handle_doctors(message: Message):
    handle_joke_genre(message, "врачи")

@bot.message_handler(func=lambda m: m.text == "👮 Менты")
def handle_cops(message: Message):
    handle_joke_genre(message, "менты")

@bot.message_handler(func=lambda m: m.text == "👩‍🏫 Школа")
def handle_school(message: Message):
    handle_joke_genre(message, "школа")

@bot.message_handler(func=lambda m: m.text == "💼 Работа")
def handle_work(message: Message):
    handle_joke_genre(message, "работа")

@bot.message_handler(func=lambda m: m.text == "👨‍💻 IT")
def handle_it(message: Message):
    handle_joke_genre(message, "программисты")

@bot.message_handler(func=lambda m: m.text == "👨‍👩‍👧‍👦 Семья")
def handle_family(message: Message):
    handle_joke_genre(message, "семья")

@bot.message_handler(func=lambda m: m.text == "🎲 Случайный")
def handle_random_joke(message: Message):
    import random
    genre = random.choice(["врачи", "менты", "школа", "работа", "программисты", "семья"])
    handle_joke_genre(message, genre)

# Ввести вручную
@bot.message_handler(func=lambda m: m.text == "✍️ Ввести жанр анекдота")
def ask_for_custom_joke_genre(message: Message):
    bot.send_message(message.chat.id, "Введите жанр анекдота, который вас интересует:")
    bot.register_next_step_handler(message, process_custom_joke_genre)

def process_custom_joke_genre(message: Message):
    user_genre = message.text.strip().lower()
    handle_joke_genre(message, user_genre)

# Назад
@bot.message_handler(func=lambda m: m.text == "🔙 Назад")
def back_to_main(message: Message):
    menu.start(message)