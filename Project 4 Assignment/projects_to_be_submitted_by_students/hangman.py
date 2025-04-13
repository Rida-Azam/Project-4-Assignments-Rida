# Project 5: Hangman Python Project

import random
import string

# Sample word list
word_list = ['python', 'hangman', 'challenge', 'programming', 'developer']

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(word_list)
    word_letters = set(word)  # Letters to guess
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Letters guessed

    lives = 6

    print("🎮 Welcome to Hangman!")
    
    # Game loop
    while len(word_letters) > 0 and lives > 0:
        # Show current state
        print("\n---------------------------------")
        print("❤️ Lives left:", lives)
        print("🔤 Letters used:", ' '.join(sorted(used_letters)))
        
        # Show word progress
        word_display = [letter if letter in used_letters else '_' for letter in word]
        print("📝 Word:", ' '.join(word_display))

        # Get user input
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("✅ Good guess!")
            else:
                lives -= 1
                print("❌ Wrong guess.")
        elif user_letter in used_letters:
            print("⚠️ You already guessed that letter.")
        else:
            print("🚫 Invalid character. Please try again.")

    # Game over
    print("\n=================================")
    if lives == 0:
        print(f"💀 You died! The word was: {word}")
    else:
        print(f"🎉 Congratulations! You guessed the word: {word}")

# Start game
hangman()
