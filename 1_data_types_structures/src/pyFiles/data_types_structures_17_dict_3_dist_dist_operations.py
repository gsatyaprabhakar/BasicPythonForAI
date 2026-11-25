## Nested Dict
financials = {
    "Q1": {"revenue": 50, "expense": 10},
    "Q2": {"revenue": 60, "expense": 30},
    "Q3": {"revenue": 55, "expense": 35},
}

# Dict Keys access
print("Dict Keys:")
for quarter in financials.keys():
    print(f"quarter: {quarter}")

print()
# Dict Values access
print("Dict Values:")
for values in financials.values():
    print(f"values: {values}")

# Nest Dict operation
# Note: Line 22 is partially visible
for quarter in financials:
    financials[quarter]['margin'] = (financials[quarter]["revenue"] - financials[quarter]["expense"]) / financials[quarter]["revenue"] * 100

print()
# Dict Key-Values access
print("Dict Key-Values access-1")
for key, values in financials.items():
    print(f"key: {key}, values: {values}")

print()
print()
print()
# Dict Key-Values access
print("Dict Key-Values access-2")
for key, values in financials.items():
    print(f"Quarter: {key}")
    for value in values:
        print(f"{value}: {values[value]:.2f}")
    print()
