from dotenv import load_dotenv
from google import genai
import requests

load_dotenv()
client = genai.Client()

# 1. get live data from the API
response = requests.get("https://api.frankfurter.app/latest?from=USD&to=INR")
rate = response.json()["rates"]["INR"]

# 2. give that data to the LLM
prompt = f'''
I have 200 NVIDIA stocks, today the price is 215$. 
How much money will I get in Indian rupees if I sell them all today.
Today's USD to INR conversion rate is {rate}
'''

try:
    answer = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    ).text
except Exception as e:
    answer = f"Something went wrong: {e}"

print(answer)
