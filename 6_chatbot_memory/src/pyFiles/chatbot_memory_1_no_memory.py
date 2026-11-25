from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

def chat(prompt):

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )
    return response.text 


print(chat("Hi! My name is Dhaval. Please remember it."))
print()

print(chat("What is my name?"))
print()
