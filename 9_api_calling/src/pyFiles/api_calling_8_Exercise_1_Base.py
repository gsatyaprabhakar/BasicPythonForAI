'''
## 🏋️ Exercise: A simple currency helper

1. Pick any two currencies (for example, EUR to INR).
2. Call the API and read the rate from the JSON.
3. Take an amount, say 100, and calculate how much it is in the other currency.
4. Print the result clearly, for example: `100 EUR = 9050 INR`.

**Bonus:** pass the converted amount to the LLM and ask it to write a one-line travel tip that mentions the amount. Now you have combined a live API with the LLM — a small but real app. 🚀
'''

import requests

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
print("10000 EUR =", 10000*float(data["rates"]["INR"]), "INR")
