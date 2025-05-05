from services.groq_client import chat_with_groq

response = chat_with_groq("Назови 5 комедийных фильмов с кратким описанием.")
print(response)