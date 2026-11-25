'''
## 🏋️ Exercise: A simple currency helper

1. Pick any two currencies (for example, EUR to INR).
2. Call the API and read the rate from the JSON.
3. Take an amount, say 100, and calculate how much it is in the other currency.
4. Print the result clearly, for example: `100 EUR = 9050 INR`.

**Bonus:** pass the converted amount to the LLM and ask it to write a one-line travel tip that mentions the amount. Now you have combined a live API with the LLM — a small but real app. 🚀
'''

import requests
from dotenv import load_dotenv
from google import genai
from google.genai import types

try:
    response = requests.get(
    "https://api.frankfurter.app/latest",
    params={"from": "EUR", "to": "INR"}
    )

    if response.status_code == 200:
        data = response.json()
        print("Rate:", data["rates"]["INR"])
    else:
        print("Something went wrong. Status code:", response.status_code)

except Exception as e:
    print("Could not reach the API:", e)

data = response.json()
print("1 EUR =", data["rates"]["INR"], "INR")

amount = 1000*float(data["rates"]["INR"])
print("1000 EUR =", amount, "INR")


load_dotenv()
client = genai.Client()

# put it in the prompt and ask
prompt = f"""
Please create a travel plan in India.
Budget: {amount} INR
Duration: 5 days
Total members: 2
"""

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt,
)

print()
print("LLM Response")
print(response)
print()
print("response.text")
print(response.text)
print()
