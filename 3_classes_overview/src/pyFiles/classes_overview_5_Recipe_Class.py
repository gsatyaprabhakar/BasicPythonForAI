from pydantic import BaseModel

# A different style of class: just LIST the fields and the type each must hold.
# No __init__, no self, no methods — Pydantic writes all that for you.
class Recipe(BaseModel):
    title: str
    calories: int
