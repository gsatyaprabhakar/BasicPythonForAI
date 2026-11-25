financials = [
    {"revenue": 50, "expenses": 10},
    {"revenue": 60, "expenses": 30},
    {"revenue": 55, "expenses": 35},
]

for fin in financials:
    profit = fin["revenue"] - fin["expenses"]
    fin['margin'] = profit * 100 / fin["revenue"]

for fin in financials:
    print(f'Revenue: {fin["revenue"]}, Expenses: {fin["expenses"]}, Margin: {fin["margin"]:.2f}%')
