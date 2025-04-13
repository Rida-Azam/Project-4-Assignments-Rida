# Project 3: Guess the Number Game Python Project (user)

import random

def computer_guesses_with_random():
    print("🤖 Think of a number between 1 and 100.")
    print("I will try to guess it! Tell me if I'm (H)igh, (L)ow, or (C)orrect.")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = random.randint(low, high)
        attempts += 1
        print(f"\nGuess #{attempts}: Is it {guess}?")
        feedback = input("Enter (H)igh, (L)ow, or (C)orrect: ").strip().upper()

        if feedback == 'C':
            print(f"🎉 Yay! I guessed your number in {attempts} tries.")
            break
        elif feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1
        else:
            print("❗ Please enter only 'H', 'L', or 'C'.")

    if low > high:
        print("\n❌ Something doesn't add up... Were you honest? 😅")

# Run the game
computer_guesses_with_random()
