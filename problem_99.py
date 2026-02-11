#Number Guessing Game: Write a Python program that generates a random number between 1 and 100 and lets the user guess the number. Use a `while` loop, `break` when the correct number is guessed, and `continue` to keep prompting the user until they guess correctly.

import random

# Generate random number between 1 and 100
secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number (1-100): "))

    if guess < secret_number:
        print("Too low! Try again.")
        continue

    if guess > secret_number:
        print("Too high! Try again.")
        continue

    print("Congratulations! You guessed correctly.")
    break
