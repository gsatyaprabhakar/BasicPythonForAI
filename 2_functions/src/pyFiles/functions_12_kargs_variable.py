def total_expenses(**kargs):
    print(kargs)
    print(type(kargs))
    print("Total", sum(kargs.values()))
    print()
    total = 0
    for key, value in kargs.items():
        total += value
    return total

total_expenses(rent=1000, phone_bill=30, food=60)

print("Two Results")
print(f'Result: {total_expenses(rent=1000, phone_bill=30)}')
print()

print("Three Results")
print(f'Result: {total_expenses(rent=1000, phone_bill=30, food=60)}')
print()

print("Four Results")
print(f'Result: {total_expenses(rent=1000, phone_bill=30, food=60, travel=100)}')
print()

print("Five Results")
print(f'Result: {total_expenses(rent=1000, phone_bill=30, food=60, travel=100, entertainment=50)}')
print()

print("Six Results")
print(f'Result: {total_expenses(rent=1000, phone_bill=30, food=60, travel=100, entertainment=50, other=20)}')
