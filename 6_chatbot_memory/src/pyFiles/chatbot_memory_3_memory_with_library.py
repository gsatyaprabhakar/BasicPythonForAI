from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()
chat_session = client.chats.create(model="gemini-3.1-flash-lite")


def chat(user_message):
    try:
        response = chat_session.send_message(user_message)
        return response.text
    except Exception as e:
        return f"Sorry, something went wrong: {e}"


print(chat("Hi! My name is Dhaval. Please remember it."))
print()

print(chat("What is my name?"))
print()
