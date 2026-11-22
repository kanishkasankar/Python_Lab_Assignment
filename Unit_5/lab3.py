# Lab Exercise 3: Dice Simulator
import random

while True:
    input("Press Enter to roll the dice (or type q to quit): ")
    # Read the quit choice from a separate prompt
    choice = input("Roll? (y/q): ").lower()
    if choice == "q":
        break
    if choice == "y":
        print("Dice result:", random.randint(1, 6))
    else:
        print("Enter y or q.")
