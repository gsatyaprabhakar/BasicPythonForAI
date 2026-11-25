revenues = [50, 60, 55]
expenses = [10, 30, 35]

print('Simple Iteration')
for rev in revenues:
    print(rev)

print()
print('Iteration with range function')
print('Value index')
for pos_index in range(len(revenues)):
    print(revenues[pos_index])

print()
print('Iteration with range function')
print('Float formatting')
print('String formatting')
print('Value index')
for pos_index in range(len(revenues)):
    profit = revenues[pos_index] - expenses[pos_index]
    margin = profit * 100 / revenues[pos_index]
    print(f"{margin:.2f}")
    print(f"Margin at index {pos_index}: {margin:.2f}%")
