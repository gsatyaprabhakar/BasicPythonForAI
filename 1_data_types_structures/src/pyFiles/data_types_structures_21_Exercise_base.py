'''
### Exercise: Codebasics Student Performance Tracker

You're tracking quiz scores for students in a Python cohort. Each student has taken 3 quizzes, and you want to figure out who's passing, who's topping, and the class average.

```
students = {
    "Aarav":   [85, 90, 78],
    "Priya":   [72, 68, 75],
    "Rohan":   [45, 52, 48],
    "Sneha":   [95, 92, 98],
    "Manish":  [60, 65, 70],
}
```

Each key is a student name, and each value is a list of 3 quiz scores (out of 100).

Write code using for loops to do the following:

1. Calculate each student's average score and print it in this format:```Aarav: 84.33```
2. Classify each student based on their average:
    80 and above → "Topper"
    60 to 79 → "Pass"
    Below 60 → "Needs improvement"
3. Find the topper of the class (highest average) and print their name and score.
4. Calculate the class average across all students.

Expected output (roughly)

```
=== Student Averages ===
Aarav: 84.33 - Topper
Priya: 71.67 - Pass
Rohan: 48.33 - Needs improvement
Sneha: 95.00 - Topper
Manish: 65.00 - Pass

=== Class Topper ===
Sneha with average 95.00

=== Class Average ===
72.87
```
'''
# Students details dictionary with their quiz scores
students = {
    "Aarav":   [85, 90, 78],
    "Priya":   [72, 68, 75],
    "Rohan":   [45, 52, 48],
    "Sneha":   [95, 92, 98],
    "Manish":  [60, 65, 70],
}

topper = []
std_avg = []

print("=== Student Averages ===")
for name, scores in students.items():
    average = sum(scores) / len(scores)
    std_avg.append(average)
    if average >= 80:
        classification = "Topper"
    elif average >= 60:
        classification = "Pass"
    else:
        classification = "Needs improvement"

    print(f"{name}: {average:.2f} - {classification}")

    if len(topper) < 1:
       topper.append(name)
       topper.append(average)
    else:
        if topper[1] < average:
            topper[0] = name
            topper[1] =average

print()
print("=== Class Topper ===")
print(f"{topper[0]} with average {topper[1]:.2f}")

print()
print("=== Class Average ===")
class_average = sum(std_avg) / len(std_avg)
print(f"{class_average:.2f}")
