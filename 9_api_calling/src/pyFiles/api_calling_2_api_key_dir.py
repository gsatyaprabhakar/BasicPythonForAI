import requests

try:
    response = requests.get(
    "https://api.frankfurter.app/latest",
    params={"api_key":"My-Key", "from": "USD", "to": "EUR"}   # now USD to Euro
    )

    if response.status_code == 200:
        print(dir(response))

except Exception as e:
    print("Could not reach the API:", e)
