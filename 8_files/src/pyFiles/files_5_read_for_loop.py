import os

# File searched at terminal current location
with open("note.txt", "r", encoding="utf-8") as f:
    print(os.path.abspath(f.name))
    for line in f:
        print(line)
