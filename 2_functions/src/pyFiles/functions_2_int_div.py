def calculate_margin(revenue, expenses):
    profit = revenue - expenses
    margin = profit * 100 // revenue
    return margin

revenue = 50
expenses = 10

margin = calculate_margin(revenue, expenses)
print(f'Margin: {margin}%')

print(f'Margin: {calculate_margin(revenue, expenses)}%')

print("Return type checking")
print(type(calculate_margin(revenue, expenses)))
print(type(margin))
