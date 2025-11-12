# 🤖 FunGenie Telegram Bot

**FunGenie** is an interactive Telegram bot built with Python and `pyTelegramBotAPI`. It offers entertainment across multiple categories, including:

- 🎬 Movies — get film suggestions by genre
- 🎵 Music — discover music recommendations
- 😂 Jokes — enjoy random or themed jokes
- 📖 Stories — read short stories by theme
- 🎮 Games — play interactive mini-games (e.g., quiz, emoji guessing, word snake)

All content is generated via AI using the **Groq API** and fine-tuned prompts.

---

## 🚀 Features

- Friendly interactive menu
- AI-generated responses with markdown formatting
- Custom genre input
- Games module with quizzes and more
- Modular code structure (`handlers/`, `services/`, etc.)

---

## 🛠 Technologies

- Python 3.10+
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- Groq API (LLM-based response generation)

---

## 📂 Project Structure
```text
FunGenie/
├── bot.py
├── funbot.py
├── config.py
├── handlers/
│ ├── menu.py
│ ├── movies.py
│ ├── music.py
│ ├── jokes.py
│ ├── stories.py
│ └── games.py
├── services/
│ ├── groq_client.py
│ ├── promts.py
│ └── utils.py
└── README.md

```

---

## ⚙️ Usage

1. Clone the repo  
2. Add your Telegram bot token to `config.py`  
3. Run the bot:


💡 Author
Created by Serhii Litus