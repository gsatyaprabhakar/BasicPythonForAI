import os
import json

# load it back — note it returns a real dict, ready to use
# File searched at terminal current location
with open("recipe.json", "r", encoding="utf-8") as f:
    print(os.path.abspath(f.name))
    loaded = json.load(f)

print(type(loaded))
print(loaded["title"])
print(loaded["ingredients"])
