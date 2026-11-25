import os
from dotenv import load_dotenv
from google import genai

# File searched at terminal current location
with open("meeting.txt", "r", encoding="utf-8") as f:
    print(os.path.abspath(f.name))
    document = f.read()

load_dotenv()
client = genai.Client()

# put it in the prompt and ask
prompt = f"""
Here is a meeting transcript:
{document}

Summarize it in 3 short bullet points.
"""

try:
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )
    summary = response.text
except Exception as e:
    summary = f"Something went wrong: {e}"

with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(summary)

print()
print(summary)
print()
print("Summary saved to summary.txt 🎉")
