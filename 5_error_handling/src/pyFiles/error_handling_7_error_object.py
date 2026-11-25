# Grab the error object with 'as e' to see the message
try:
    age = int("twenty")
except ValueError as e:
    print("Couldn't convert to a number.")
    print("Technical detail:", e)
