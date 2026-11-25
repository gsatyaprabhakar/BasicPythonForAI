# Red, Green, Blue
purple = (128, 0, 128)

print("purple")
print(purple)

r,b,g = purple
print(f'r: {r}')
print(f'b: {b}')
print(f'g: {g}')
print()

yellow = (255, 255, 0)
print("yellow")
print(yellow)
print()

print("Int Mix")
mixed = (purple[0] + yellow[0])//2,  (purple[1] + yellow[1])//2, (purple[2] + yellow[2])//2
print("mixed")
print(mixed)
print()
