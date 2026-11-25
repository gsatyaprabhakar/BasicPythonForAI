from classes_overview_5_Recipe_Class import Recipe

print("First")
# Build one like any other object:
dal = Recipe(title="Yellow Dal", calories=280)
print(dal.title)
print(dal.calories)
print()

print("Second")
dal = Recipe(calories=280,title="Yellow Dal")
print(dal.title)
print(dal.calories)
print()
