fin = {"revenue": 50, "expenses": 10}

print('Data Type')
print(type(fin))
print()

print('Size/Length')
print(len(fin))
print()


print('Contents')
print(fin)
print()

profit = fin["revenue"] - fin["expenses"]
margin = profit * 100 / fin["revenue"]
print(f'Margin: {margin:.2f}%')
