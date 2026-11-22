# Lab Exercise 2: Prime Number and Factorial
number = int(input("Enter a positive integer: "))

# Prime number check
if number > 1:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    print("Prime number" if is_prime else "Not a prime number")
else:
    print("Not a prime number")

# Factorial
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print("Factorial =", factorial)
