def calc_total_expense(*args):
    print(args)
    print(type(args))
    return sum(args)

print("Two Results")
print(f'Result: {calc_total_expense(2,3) }')
print()

print("Three Results")
print(f'Result: {calc_total_expense(2,3,4) }')
print()

print("Four Results")
print(f'Result: {calc_total_expense(2,3,4,5) }')
print()

print("Five Results")
print(f'Result: {calc_total_expense(2,3,4,5,6) }')
print()

print("Six Results")
print(f'Result: {calc_total_expense(2,3,4,5,6,7) }')
