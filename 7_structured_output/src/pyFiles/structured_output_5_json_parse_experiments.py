from dotenv import load_dotenv
from google import genai
import json

load_dotenv()
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents='''Give me a simple Indian dal recipe.
    Return ONLY JSON with these keys: title, calories, prep_time_minutes.'''
)

print(response.text)    # 👀 look closely at how it starts and ends...

# Expected but some additional character before and after, but output looks like a VALID JSON some times
# Behaviour is is NOT consistent.
# Program is breaking somewhere even when output format as Output-1
# 
# Output-1 :
# {
#   "title": "Simple Yellow Dal Tadka",
#   "calories": 180,
#   "prep_time_minutes": 25
# }
# 
# Output-2 :
# ```json
# {
#   "title": "Simple Yellow Dal Tadka",
#   "calories": 180,
#   "prep_time_minutes": 25
# }
# ```


print()
try:
    # As expected output format Not consistant, below code is working without any error for Output-1
    # Looks like JSON, so let's parse it:
    data = json.loads(response.text)   # 💥 JSONDecodeError!
    print(data)
    print(type(data))
    print()
    print("Printing details from above data object")
    print("Title:", data.title)
    print("Calories:", data.calories)        # a real int
    print("Prep time:", data.prep_time_minutes, "min")
    print("Printing details from above data object - Successful !!!")
except Exception as e:
    print("Printing details from above data object - NOT Successful !!!")
    print("Exception Details: ", e)

print()
try:
    print("response.parsed ")
    recipe = response.parsed     # a Recipe object, parsed for us
    print(recipe)
    print(type(recipe))
    print("Title:", recipe.title)
    print("Calories:", recipe.calories)        # a real int
    print("Prep time:", recipe.prep_time_minutes, "min")
    print("response.parsed  - Successful !!!")
except Exception as e:
    print("response.parsed  - NOT Successful !!!")
    print("Exception Details: ", e)

print()
try:
    print("Experimenting")
    print(response.text)
    print(type(response.text))
    print("Title:", response.text.title)
    print("Calories:", response.text.calories)        # a real int
    print("Prep time:", response.text.recipe.prep_time_minutes, "min")
    print("Experiment - Successful !!!")
except Exception as e:
    print("Experiment - NOT Successful !!!")
    print("Exception Details: ", e)

print("Check Execution Results")




# {
#   "title": "Simple Yellow Dal Tadka",
#   "calories": 180,
#   "prep_time_minutes": 25
# }
# 
# {'title': 'Simple Yellow Dal Tadka', 'calories': 180, 'prep_time_minutes': 25}
# <class 'dict'>
# 
# Printing details from above data object
# Printing details from above data object - NOT Successful !!!
# Exception Details:  'dict' object has no attribute 'title'
# 
# response.parsed 
# None
# <class 'NoneType'>
# response.parsed  - NOT Successful !!!
# Exception Details:  'NoneType' object has no attribute 'title'
# 
# Experimenting
# {
#   "title": "Simple Yellow Dal Tadka",
#   "calories": 180,
#   "prep_time_minutes": 25
# }
# <class 'str'>
# Title: <built-in method title of str object at 0x0000019C244A3D30>
# Experiment - NOT Successful !!!
# Exception Details:  'str' object has no attribute 'calories'
# Check Execution Results
