'''
## 🏋️ Exercise: Meeting notes → action items

Build a little tool that turns messy meeting notes into a saved to-do list.

1. Reuse the `meeting.txt` file from Part 3 (or write your own).
2. Read it, and ask the LLM to **extract the action items** — who needs to do what.
3. Save the result to `action_items.txt`.

**Bonus (ties everything together):** instead of plain text, ask for **structured output** (a Pydantic model with a list of `{task, owner}`), then save it with `json.dump` to `action_items.json`. Load it back and print each task. Now you've combined files + structured output into one mini-app. 🚀
'''

import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel

class ActionItem(BaseModel):
    task: str
    owner: str

class ActionItems(BaseModel):
    action_items: list[ActionItem]

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

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt,
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=ActionItems,
    ),
)

print()
print("LLM Response")
print(response)
print()

parsed = response.parsed
if parsed is None:
    raise ValueError("The model response did not contain valid structured action items.")

print()
print("parsed = response.parsed")
print(parsed)
print()

print()
print('parsed.model_dump(mode="json")')
print(parsed.model_dump(mode="json"))
print()

# save the dict as a .json file
# This file created at terminal current location
with open("action_items.json", "w", encoding="utf-8") as f:
    print(os.path.abspath(f.name))
    json.dump(parsed.model_dump(mode="json"), f, indent=2)

print()
print("action_items.json saved.")
print()


# load it back — note it returns a real dict, ready to use
# File searched at terminal current location
with open("action_items.json", "r", encoding="utf-8") as f:
    print(os.path.abspath(f.name))
    loaded = json.load(f)


print()
print("action_items.json content")
print(loaded)
print()

for item in loaded["action_items"]:
    print(f"{item['task']} (owner: {item['owner']})")


print()
print()
print("Completed Execution")
print()
