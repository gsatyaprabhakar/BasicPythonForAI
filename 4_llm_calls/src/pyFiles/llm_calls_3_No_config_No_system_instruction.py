from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="Tell me who invented Samosa in 3 lines."
)
print(response.text)
