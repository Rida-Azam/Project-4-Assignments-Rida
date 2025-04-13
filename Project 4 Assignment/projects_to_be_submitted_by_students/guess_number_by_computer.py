# Project 2: Guess the Number Game Python Project (computer)

import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    print("🎮 Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} guesses to find it.\n")

    while attempts < max_attempts:
        guess = input(f"Guess #{attempts + 1}: ")

        if not guess.isdigit():
            print("❗ Please enter a valid number.\n")
            continue

        guess = int(guess)
        attempts += 1
        guesses_left = max_attempts - attempts

        if guess < secret_number:
            print(f"🔻 Too low! You have {guesses_left} guesses left.\n")
        elif guess > secret_number:
            print(f"🔺 Too high! You have {guesses_left} guesses left.\n")
        else:
            print(f"🎉 Correct! You guessed the number in {attempts} tries.")
            return

    # If loop ends without correct guess
    print(f"😢 Out of guesses! The number was {secret_number}.")

# Run the game
guess_the_number()
