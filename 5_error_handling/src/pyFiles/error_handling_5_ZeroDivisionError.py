revenue = 0
expenses = 10

try:
    margin = (revenue - expenses) * 100 / revenue
    print(f"Margin: {margin:.2f}%")
except ZeroDivisionError:
    print("Revenue is 0, can't calculate margin. Skipping.")

print("Program keeps running 🎉")
