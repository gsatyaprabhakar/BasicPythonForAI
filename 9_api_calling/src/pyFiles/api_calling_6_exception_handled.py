import requests

try:
    response = requests.get(
    "https://api.frankfurter.app/latest",
    params={"from": "USD", "to": "EUR"}   # now USD to Euro
    )

    if response.status_code == 200:
        data = response.json()
        print("Rate:", data["rates"]["EUR"])
    else:
        print("Something went wrong. Status code:", response.status_code)

except Exception as e:
    print("Could not reach the API:", e)

data = response.json()
print("1 USD =", data["rates"]["EUR"], "EUR")
