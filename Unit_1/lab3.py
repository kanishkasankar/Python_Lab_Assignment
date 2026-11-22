# Lab Exercise 3: Simple Calculator and Area Calculations
print("1. Calculator")
print("2. Area of a rectangle")
print("3. Area of a circle")
choice = input("Enter your choice: ")

if choice == "1":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")
    if op == "+":
        print("Result =", a + b)
    elif op == "-":
        print("Result =", a - b)
    elif op == "*":
        print("Result =", a * b)
    elif op == "/":
        if b != 0:
            print("Result =", a / b)
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid operator")
elif choice == "2":
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    print("Area =", length * breadth)
elif choice == "3":
    radius = float(input("Enter radius: "))
    print("Area =", 3.14159 * radius * radius)
else:
    print("Invalid choice")
