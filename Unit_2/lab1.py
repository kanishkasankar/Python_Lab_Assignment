# Lab Exercise 1: Number Guessing Game
import random

secret = random.randint(1, 20)
attempts = 0
print("Guess a number between 1 and 20!")

while True:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess == secret:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
    elif guess < secret:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
