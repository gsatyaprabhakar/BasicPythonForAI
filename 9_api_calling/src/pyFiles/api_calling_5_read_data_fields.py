import requests

# This URL asks: "give me the latest rate from USD to INR"
url = "https://api.frankfurter.app/latest?from=USD&to=INR"


response = requests.get(url)
print(response.status_code)   # 200 means "OK, it worked"


data = response.json()
print(type(data))   # it is just a dict!
print(data)


rate = data["rates"]["INR"]
print(f"Today, 1 US Dollar = {rate} Indian Rupees")
