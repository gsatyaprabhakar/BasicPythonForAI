import os

# File searched at terminal current location
with open("meeting.txt", "r", encoding="utf-8") as f:
    print(os.path.abspath(f.name))
    content = f.read()

print(content)
