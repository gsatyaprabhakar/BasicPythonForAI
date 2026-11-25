import os

# This file created at terminal current location
with open("note.txt", "w", encoding="utf-8") as f:
    print(os.path.abspath(f.name))
    f.write("My memory is so bad.\n")
    f.write("How bad is it?\n")
    f.write("How bad is what?\n")

print("Saved! Open note.txt to read the joke.")
