revenue = 43
expenses = 11

profit = revenue-expenses
margin_int = profit * 100 // revenue
margin_float = profit * 100 / revenue

print('margin_int:', margin_int)
print('margin_float:', margin_float)
print()


# Red, Green, Blue
purple = (128, 0, 128)

print("purple")
print(purple)
print()

yellow = (255, 255, 0)
print("yellow")
print(yellow)
print()

print("Int Mix")
mixed = (purple[0] + yellow[0])//2,  (purple[1] + yellow[1])//2, (purple[2] + yellow[2])//2
print("mixed")
print(mixed)
print()

print("Float Mix")
mixed = (purple[0] + yellow[0])/2,  (purple[1] + yellow[1])/2, (purple[2] + yellow[2])/2
print("mixed")
print(mixed)
print()
print()
print()


revenues = [50, 60, 55]
expenses = [15, 35, 30]

print("revenues")
print(revenues)
print()

print("expenses")
print(expenses)
print()

print("Int Mix")
mixed = (revenues[0] + expenses[0])//2,  (revenues[1] + expenses[1])//2, (revenues[2] + expenses[2])//2
print("mixed")
print(mixed)
print()

print("Float Mix")
mixed = (revenues[0] + expenses[0])/2,  (revenues[1] + expenses[1])/2, (revenues[2] + expenses[2])/2
print("mixed")
print(mixed)
print()
