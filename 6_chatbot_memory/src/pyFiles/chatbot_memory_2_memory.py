from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

conversation = []   # this list IS the chatbot's memory

def chat(user_message):
    # 1. add what the user said to memory
    conversation.append({"role": "user", "parts": [{"text": user_message}]})

    # 2. send the ENTIRE conversation so far
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=conversation
        )
        reply = response.text
    except Exception as e:
        return f"Sorry, something went wrong: {e}"

    # 3. add the AI's reply to memory too, so it remembers next time
    conversation.append({"role": "model", "parts": [{"text": reply}]})
    return reply


print(chat("Hi! My name is Dhaval. Please remember it."))
print()

print(chat("What is my name?"))
print()

print("Conversation so far:")
for message in conversation:
    print(message["role"], "->", message["parts"][0]["text"])
    print()
