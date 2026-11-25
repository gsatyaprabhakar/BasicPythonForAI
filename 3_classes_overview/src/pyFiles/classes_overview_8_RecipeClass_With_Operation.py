from pydantic import BaseModel

# A different style of class: just LIST the fields and the type each must hold.
# No __init__, no self, no methods — Pydantic writes all that for you.
class Recipe(BaseModel):
    title: str
    calories: int

    def print_recipe(self):
        print(f"Recipe: {self.title}, Calories: {self.calories}")

    def is_healthy(self):
        return self.calories < 300


# Build one like any other object:
dal = Recipe(title="Yellow Dal", calories=280)
dal.print_recipe()
print(dal.title)
print(dal.calories)
if dal.is_healthy():
    print("This recipe is healthy.")
else:
    print("This recipe is not healthy.")
