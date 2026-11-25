import requests

# This URL asks: "give me the latest rate from USD to INR"
url = "https://api.frankfurter.app/latest?from=USD&to=INR"

response = requests.get(url)

print(response.status_code)   # 200 means "OK, it worked"
