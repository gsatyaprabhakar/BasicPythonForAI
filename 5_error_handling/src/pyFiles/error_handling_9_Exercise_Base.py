'''
## Exercise: Codebasics Chai Stall — Resilient Bill Calculator

Remember the chai bill calculator from lesson 2? Customers (and bugs) don't always behave. Make it bulletproof.

Write a function `safe_chai_bill(cups, price_per_cup)` that:
1. Converts `cups` and `price_per_cup` to numbers using `int()` / `float()` (they may arrive as text from a form).
2. Uses `try/except` to catch a `ValueError` if someone passes `"two"` instead of `2` → return the message `"Please enter numbers only."`
3. If `cups` is less than 1, return the message `"Cups must be at least 1"`.
4. Otherwise return the total bill (`cups * price_per_cup`).

Test it with these calls:
```python
print(safe_chai_bill("3", "15"))     # normal text input from a form
print(safe_chai_bill(2, 15))          # normal numbers
print(safe_chai_bill("two", 15))      # bad input -> caught
print(safe_chai_bill(0, 15))          # too few cups
```

Expected (roughly):
```
45
30
Please enter numbers only.
Cups must be at least 1
```

**Bonus:** wrap the call in lesson 3's Streamlit app so a bad recipe request shows `st.error(...)` instead of crashing.
'''

def safe_chai_bill(cups, price_per_cup):

    try:
    #    print("cups checking")
    #    cups_float = float(cups)
        cups_float = int(cups)
    #    print("price_per_cup checking")
    #    price_per_cup_float = float(price_per_cup)
        price_per_cup_float = int(price_per_cup)

        if cups_float > 0:
            return cups_float*price_per_cup_float
        return "Cups must be at least 1"

    except ValueError as e:
    #    print("Please enter numbers only.")
    #    print("Error Detail:", e)
        return "Please enter numbers only."


print(safe_chai_bill("3", "15"))      # normal text input from a form
print(safe_chai_bill(2, 15))          # normal numbers
print(safe_chai_bill("two", 15))      # bad input -> caught
print(safe_chai_bill(0, 15))          # too few cups
