# Lab Exercise 1: Bank Account System Using OOP
class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
        else:
            print("Amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Invalid amount or insufficient balance.")

    def display(self):
        print(f"Account holder: {self.holder}")
        print(f"Balance: ₹{self.balance:.2f}")

name = input("Account holder name: ")
account = BankAccount(name)

while True:
    print("\ n1. Deposit  2. Withdraw  3. Display  4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        account.deposit(float(input("Amount: ")))
    elif choice == "2":
        account.withdraw(float(input("Amount: ")))
    elif choice == "3":
        account.display()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
