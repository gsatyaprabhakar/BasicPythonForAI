import os
from dotenv import load_dotenv

print(load_dotenv())
print(os.getenv("GOOGLE_API_KEY"))
print(os.getenv("OPENAI_API_KEY"))
print(os.getenv("GROQ_API_KEY"))
