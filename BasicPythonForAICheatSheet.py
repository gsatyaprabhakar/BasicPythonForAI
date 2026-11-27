######################################################
import sys

######################################################
print(sys.version)

######################################################
try:
    import pydantic  # type: ignore[import-not-found]
    print("pydantic imported successfully")
except ImportError:
    pydantic = None

######################################################
if pydantic is not None:
    print(pydantic.__version__)
else:
    print("pydantic not installed")

######################################################
type(margin)

######################################################
revenues = [50, 60, 55]

######################################################
len(revenues)

######################################################
for rev in revenues:
    print(rev)

######################################################
print(f'Margin (formatted): {margin:.2f}')      # Single cote
print(f"Margin (formatted): {margin:.2f}")      # Double cote

######################################################
for i in range(len(revenues)):
    profit = revenues[i] - expenses[i]

######################################################
margins = []
margins.append(margin)

######################################################
fin = {"revenue": 50, "expenses": 10}

######################################################
financials = [
    {"revenue": 50, "expenses": 10},
    {"revenue": 60, "expenses": 30},
    {"revenue": 55, "expenses": 35}
]

for fin in financials:
    profit = fin["revenue"] - fin["expenses"]
    fin['margin'] = profit * 100 / fin["revenue"]

######################################################
financials = {
    "Q1": {"revenue": 50, "expense": 10},
    "Q2": {"revenue": 60, "expense": 30},
    "Q3": {"revenue": 55, "expense": 35},
}
# Dict Keys access
print("Dict Keys:")
for quarter in financials.keys():
    print(f"quarter: {quarter}")
print()
# Dict Values access
print("Dict Values:")
for values in financials.values():
    print(f"values: {values}")
print()
# Dict Key-Values access
print("Dict Key-Values access-1")
for key, values in financials.items():
    print(f"key: {key}, values: {values}")

######################################################
purple = (128, 0, 128)
r, g, b = purple
revenues = [50, 60, 55]
a, b, c = revenues

######################################################
expenses = [50, 60, 55, 78, 89, 59, 65, 93, 99]
print(expenses[-3])
print(expenses[-2])
print(expenses[-1])
for rev in expenses[2:8]:   # Iterate from 2nd index to 7th index

######################################################
revenues = [50, 60, 55]
expenses = [15, 35, 30]
mixed = (revenues[0] + expenses[0])/2,  (revenues[1] + expenses[1])/2, (revenues[2] + expenses[2])/2
mixed = (revenues[0] + expenses[0])//2,  (revenues[1] + expenses[1])//2, (revenues[2] + expenses[2])//2

######################################################
continue

######################################################
if discount_percent:
if data["revenue"] < 0:

######################################################
students = {
    "Aarav":   [85, 90, 78],
    "Priya":   [72, 68, 75],
    "Rohan":   [45, 52, 48],
    "Sneha":   [95, 92, 98],
    "Manish":  [60, 65, 70],
}
for name, scores in students.items():
    average = sum(scores) / len(scores)
    std_avg.append(average)

######################################################
class_topper_average = float("-inf")

######################################################
def calculate_margin(revenue, expenses):
    profit = revenue - expenses
    margin = profit * 100 / revenue
    return margin

######################################################
def calculate_profit_and_margin(revenue, expenses):
    profit = revenue - expenses
    margin = profit * 100 / revenue
    return profit, margin

def calculate_profit_and_margin(revenue, expenses):
    profit = revenue - expenses
    margin = profit * 100 / revenue
    return (profit, margin)

def calculate_profit_and_margin(revenue, expenses):
    profit = revenue - expenses
    margin = profit * 100 / revenue
    return [profit, margin]

######################################################
def calculate_margin(revenue: float, expenses: float) -> float:
    profit = revenue - expenses
    return profit * 100 / revenue

######################################################
def double(x: int) -> int:
    return x * 2

######################################################
def get_total_expense(*args):
    print(args)
    print(type(args))
    return sum(args)

######################################################
def get_total_expenses(**kargs):
    print(kargs)
    print(type(kargs))
    ## return sum(kargs.values())   # This is more efficient
    total = 0
    for key, value in kargs.items():
        total += value
    return total

######################################################
discount_percent = discount.get("discount_percent", 0)

######################################################
if not isinstance(cups, int) or cups < 0:
if not isinstance(addon, str):
if not isinstance(discount_percent, (int, float)):

######################################################
unsupported_keys = set(discount) - {"discount_percent"}

######################################################
raise TypeError(f"Unsupported keyword arguments: {sorted(unsupported_keys)}")

######################################################
if __name__ == "__main__":

######################################################
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.10

######################################################
from pydantic import BaseModel

class Recipe(BaseModel):
    title: str
    calories: int

class Recipe(BaseModel):
    title: str
    calories: int

    def print_recipe(self):
        print(f"Recipe: {self.title}, Calories: {self.calories}")

    def is_healthy(self):
        return self.calories < 300

######################################################
dal = Recipe(title="Yellow Dal", calories=280)

######################################################
from class_3_Employee_class_defi import Employee

######################################################
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

def generate_recipe(ingradients, cuisine, diet):
    '''
    Generate a recipe using ingradients provided. 
    Cuisine can be "Italian", "Mexican", "Indian", "Any" etc.
    diet can be "Vegan", "Vegeterian", "Jain", "Any" etc.
    '''
    
    prompt = f'''
    Generate one food receipe using these ingradients: {','.join(ingradients)}
    Receipe should not be more than 100 words
    Cuisine: {cuisine}
    Diet: {diet}
    '''
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction="You are a helpful assistant who specializes in food history."
        ),
        contents=prompt
    )
    return response.text 

print(generate_recipe(["Tomatoes", "lentils", "onion", "jeera", "salt"],"Indian","Vegan"))

######################################################
','.join(ingradients)

######################################################
try:
    age = int("twenty")
except ValueError as e:
    print("Couldn't convert to a number.")

######################################################
if not response.text:

######################################################
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

######################################################
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

######################################################
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel

# This class IS the shape we want back. Note the types: str, int, list of str.
class Recipe(BaseModel):
    title: str
    calories: int
    ingredients: list[str]
    prep_time_minutes: int

load_dotenv()
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="Give me a simple Indian dal recipe.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",    # "reply in JSON"
        response_schema=Recipe,                   # "...in exactly THIS shape"
    ),
)

print(response.text)   # guaranteed-clean JSON string
print()

recipe = response.parsed     # a Recipe object, parsed for us

print("Title:", recipe.title)
print("Calories:", recipe.calories)        # a real int
print("Prep time:", recipe.prep_time_minutes, "min")

print()
print("Ingredients:")
for item in recipe.ingredients:            # a real list we can loop over!
    print(" -", item)

######################################################
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

parsed = response.parsed
if parsed is None:
    raise ValueError("The model response did not contain valid structured action items.")

# save the dict as a .json file
# This file created at terminal current location
with open("action_items.json", "w", encoding="utf-8") as f:
    print(os.path.abspath(f.name))
    json.dump(parsed.model_dump(mode="json"), f, indent=2)

# load it back — note it returns a real dict, ready to use
# File searched at terminal current location
with open("action_items.json", "r", encoding="utf-8") as f:
    print(os.path.abspath(f.name))
    loaded = json.load(f)

######################################################
import requests

response = requests.get(
    "https://api.frankfurter.app/latest",
    params={"from": "USD", "to": "EUR"}   # now USD to Euro
)

print(response.status_code) 

print(dir(response))

data = response.json()
print("1 USD =", data["rates"]["EUR"], "EUR")


######################################################
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
client = genai.Client()


app = FastAPI()


# -------------------------------------------------------------------
# Open http://127.0.0.1:8000/ in the browser to see this.
# -------------------------------------------------------------------
@app.get("/")
def home():
    return {"message": "Welcome, How Are You?"}


# -------------------------------------------------------------------
# Try: http://127.0.0.1:8000/margin?revenue=5000&expenses=3000
# Notice the type hints (revenue: float). FastAPI uses them to read the
# inputs from the URL and turn the text into numbers for us.
# -------------------------------------------------------------------
@app.get("/margin")
def margin(revenue: float, expenses: float):
    profit = revenue - expenses
    margin_percent = (profit / revenue) * 100
    return {"profit": profit, "margin_percent": margin_percent}


# What the user must SEND us (the request body)
class Review(BaseModel):
    text: str


# What Gemini must give back, and what we SEND to the user (the response)
class Sentiment(BaseModel):
    label: str   # "positive", "negative", or "neutral"
    score: int   # 1 (very bad) to 5 (very good)


@app.post("/sentiment")
def analyze_sentiment(review: Review):
# def analyze_sentiment(review: Review) -> Sentiment : ## Validate it
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=(
            "Find the sentiment of this customer review. "
            "label must be 'positive', 'negative', or 'neutral'. "
            "score must be a number from 1 (very bad) to 5 (very good). "
            f"Review: {review.text}"
        ),
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Sentiment,
        ),
    )
    # response.parsed is already a Sentiment object, ready to return.
    return response.parsed


######################################################
from project_feedback_analyzer_1_database import init_db, save_results, load_history, DB_FILE

######################################################
