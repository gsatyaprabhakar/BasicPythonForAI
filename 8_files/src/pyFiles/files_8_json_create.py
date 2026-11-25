import os
import json

recipe = {
    "title": "Yellow Dal",
    "calories": 280,
    "ingredients": ["lentils", "onion", "tomato", "cumin"]
}

# save the dict as a .json file
# This file created at terminal current location
with open("recipe.json", "w", encoding="utf-8") as f:
    print(os.path.abspath(f.name))
    json.dump(recipe, f, indent=2)

print("recipe.json saved.")
