# Project 4: Rock, paper, scissors Python Project


import random
import random

def get_user_choice():
    choice = input("Choose rock, paper, or scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("❗ Invalid choice.")
        choice = input("Please choose rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "🎉 You win!"
    else:
        return "💻 Computer wins!"

def play_game():
    print("🪨 Welcome to Rock, Paper, Scissors! ✂️")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\n🧑 You chose: {user_choice}")
    print(f"🤖 Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(f"\n{result}")

# Start the game
play_game()
