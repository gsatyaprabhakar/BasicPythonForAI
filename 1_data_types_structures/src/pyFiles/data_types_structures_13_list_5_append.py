revenues = [50, 60, 55]
expenses = [10, 30, 35]

margins_normal = []
margins_formatted = []
for pos_index in range(len(revenues)):
    profit = revenues[pos_index] - expenses[pos_index]
    margin = profit * 100 / revenues[pos_index]
    margins_normal.append(margin)
    margins_formatted.append(f"{margin:.2f}")

for pos_index in range(len(margins_normal)):
    print(f"margins_normal at index {pos_index}: {margins_normal[pos_index]}%")
    print(f"margins_normal (Formatted) at index {pos_index}: {margins_normal[pos_index]:.2f}%")
    print(f"margins_formatted at index {pos_index}: {margins_formatted[pos_index]}%")
