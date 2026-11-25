# Employee 1
name1 = "Mohan"
salary1 = 80000

# Employee 2
name2 = "Fatima"
salary2 = 95000

def calculate_bonus(salary):
    return salary * 0.10

print(f"{name1}'s bonus: {calculate_bonus(salary1)}")
print(f"{name2}'s bonus: {calculate_bonus(salary2)}")
