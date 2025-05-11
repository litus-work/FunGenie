from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
from funbot import bot
from services.groq_client import chat_with_groq
from services.utils import remove_think_blocks
from services.promts import story_prompt
from handlers import menu


@bot.message_handler(func=lambda m: "Истори" in m.text)
def handle_stories(message: Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(KeyboardButton("🧛 Мистика"), KeyboardButton("❤️ Любовные"))
    markup.row(KeyboardButton("😂 Забавные"), KeyboardButton("🤯 Неожиданные"))
    markup.row(KeyboardButton("🧠 Поучительные"), KeyboardButton("🌍 Из жизни"))
    markup.row(KeyboardButton("🎲 Случайная"), KeyboardButton("🔙 Назад"))
    markup.row(KeyboardButton("✍️ Ввести жанр истории"))

    bot.send_message(message.chat.id, "Выбери жанр истории 📖", reply_markup=markup)


def handle_story_genre(message: Message, genre: str):
    prompt = story_prompt(genre)
    bot.send_chat_action(message.chat.id, 'typing')
    response = chat_with_groq(prompt)
    cleaned = remove_think_blocks(response)
    bot.send_message(message.chat.id, cleaned, parse_mode='Markdown')


@bot.message_handler(func=lambda m: m.text == "🧛 Мистика")
def handle_mystic(message: Message):
    handle_story_genre(message, "мистика")

@bot.message_handler(func=lambda m: m.text == "❤️ Любовные")
def handle_love(message: Message):
    handle_story_genre(message, "любовные")

@bot.message_handler(func=lambda m: m.text == "😂 Забавные")
def handle_funny(message: Message):
    handle_story_genre(message, "забавные")

@bot.message_handler(func=lambda m: m.text == "🤯 Неожиданные")
def handle_twist(message: Message):
    handle_story_genre(message, "с неожиданным концом")

@bot.message_handler(func=lambda m: m.text == "🧠 Поучительные")
def handle_moral(message: Message):
    handle_story_genre(message, "поучительные")

@bot.message_handler(func=lambda m: m.text == "🌍 Из жизни")
def handle_life(message: Message):
    handle_story_genre(message, "жизненные")

@bot.message_handler(func=lambda m: m.text == "🎲 Случайная")
def handle_random_story(message: Message):
    import random
    genre = random.choice(["мистика", "любовные", "забавные", "жизненные", "поучительные", "с неожиданным концом"])
    handle_story_genre(message, genre)


@bot.message_handler(func=lambda m: m.text == "✍️ Ввести жанр истории")
def ask_for_custom_story_genre(message: Message):
    bot.send_message(message.chat.id, "Введите жанр истории, который вас интересует:")
    bot.register_next_step_handler(message, process_custom_story_genre)

def process_custom_story_genre(message: Message):
    user_genre = message.text.strip().lower()
    handle_story_genre(message, user_genre)


@bot.message_handler(func=lambda m: m.text == "🔙 Назад")
def back_to_main(message: Message):
    menu.start(message)
