'''
## 🏋️ Exercise: Meeting notes → action items

Build a little tool that turns messy meeting notes into a saved to-do list.

1. Reuse the `meeting.txt` file from Part 3 (or write your own).
2. Read it, and ask the LLM to **extract the action items** — who needs to do what.
3. Save the result to `action_items.txt`.

**Bonus (ties everything together):** instead of plain text, ask for **structured output** (a Pydantic model with a list of `{task, owner}`), then save it with `json.dump` to `action_items.json`. Load it back and print each task. Now you've combined files + structured output into one mini-app. 🚀
'''

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

**extract the action items** — who needs to do what.
"""

try:
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )
    action_items = response.text
except Exception as e:
    action_items = f"Something went wrong: {e}"

with open("action_items.txt", "w", encoding="utf-8") as f:
    f.write(action_items)

print()
print(action_items)
print()
print("Action items saved to action_items.txt 🎉")
