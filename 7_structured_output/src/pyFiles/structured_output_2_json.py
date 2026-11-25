from dotenv import load_dotenv
from google import genai

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
