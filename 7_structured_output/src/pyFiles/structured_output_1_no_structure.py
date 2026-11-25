from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="Give me a simple Indian dal recipe (in less than 10 lines) with its calorie count."
)

print(response.text)
