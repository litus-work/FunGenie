from funbot import bot

# Регистрируем хендлеры
from handlers import menu, movies, music

if __name__ == '__main__':
    print("🤖 Бот запущен...")
    try:
        bot.infinity_polling()
    except Exception as e:
        print("❌ Произошла ошибка при запуске бота:")
        print(e)
