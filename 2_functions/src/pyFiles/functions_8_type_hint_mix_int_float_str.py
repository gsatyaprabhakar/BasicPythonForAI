def double(x: int) -> int:
    return x * 2

print("Integer")
result = double(5)
print(f'Doubled value: {result}')
print("Return type checking")
print(type(double(5)))
print(type(result))
print()

print("Float")
result = double(5.7)
print(f'Doubled value: {result}')
print("Return type checking")
print(type(double(5.7)))
print(type(result))
print()

print("String")
result = double('Hello')
print(f'Doubled value: {result}')
print("Return type checking")
print(type(double('Hello')))
print(type(result))
print()
