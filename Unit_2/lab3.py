# Lab Exercise 3: Fibonacci Series Using Recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("How many terms? "))
if terms <= 0:
    print("Enter a positive number of terms.")
else:
    print("Fibonacci series:")
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()
