from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel

# This class IS the shape we want back. Note the types: str, int, list of str.
class Recipe(BaseModel):
    title: str
    ingredients: list[str]
    calories: int
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

# Output
# {
#   "title": "Simple Yellow Dal",
#   "ingredients": [
#     "1 cup yellow moong dal",
#     "3 cups water",
#     "1 tsp turmeric powder",
#     "1 tsp salt",
#     "2 tbsp ghee",
#     "1 tsp cumin seeds",
#     "2 cloves garlic minced",
#     "1 chopped tomato"
#   ],
#   "calories": 220,
#   "prep_time_minutes": 25
# }

recipe = response.parsed     # a Recipe object, parsed for us

print("Title:", recipe.title)
print("Calories:", recipe.calories)        # a real int
print("Prep time:", recipe.prep_time_minutes, "min")

print()
print("Ingredients:")
for item in recipe.ingredients:            # a real list we can loop over!
    print(" -", item)

# Output
# Title: Simple Yellow Dal
# Calories: 220
# Prep time: 25 min
#
# Ingredients:
#  - 1 cup yellow moong dal
#  - 3 cups water
#  - 1 tsp turmeric powder
#  - 1 tsp salt
#  - 2 tbsp ghee
#  - 1 tsp cumin seeds
#  - 2 cloves garlic minced
#  - 1 chopped tomato
