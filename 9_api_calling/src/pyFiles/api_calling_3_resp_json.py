import requests

response = requests.get(
    "https://api.frankfurter.app/latest",
    params={"from": "USD", "to": "EUR"}   # now USD to Euro
)

data = response.json()
print("1 USD =", data["rates"]["EUR"], "EUR")
