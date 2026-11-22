# Lab Exercise 2: Variables, Operators, Input and Output
name = input("Enter your name: ")
age = int(input("Enter your age: "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\\nHello {name}!")
print(f"Your age is {age}")
print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
if num2 != 0:
    print(f"Division: {num1 / num2}")
else:
    print("Division is not possible by zero.")
