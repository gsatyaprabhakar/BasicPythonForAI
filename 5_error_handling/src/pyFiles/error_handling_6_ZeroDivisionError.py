def safe_margin(revenue, expenses):
    try:
        return (revenue - expenses) * 100 / revenue
    except ZeroDivisionError:
        return None   # signal "couldn't compute"

print(safe_margin(50, 10))
print(safe_margin(0, 10))
