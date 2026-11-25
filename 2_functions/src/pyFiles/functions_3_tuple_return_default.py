def calculate_profit_and_margin(revenue, expenses):
    profit = revenue - expenses
    margin = profit * 100 / revenue
    return profit, margin

revenue = 50
expenses = 10

print("Approach-1: Using Tuple Unpacking")
profit, margin = calculate_profit_and_margin(revenue, expenses)
print(f'Profit: {profit}')
print(f'Margin: {margin:.2f}%')
print()

print("Approach-2: Using Indexing")
result = calculate_profit_and_margin(revenue, expenses)
print(f'Profit: {result[0]}')
print(f'Margin: {result[1]:.2f}%')
print()

print("Return type checking")
print(type(result))
print(type(calculate_profit_and_margin(revenue, expenses)))
