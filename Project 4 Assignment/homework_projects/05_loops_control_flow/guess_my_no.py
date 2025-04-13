# Problem Statement

# Guess My Number

import random

def main():
  secretNumber = random.randint(0, 99)

  print("I am thinking of a number between 0 and 99...")
  guess = int(input("Enter a guess: "))

  while guess != secretNumber:
   if guess < secretNumber:
    print("Your guess is too low")
    guess = int(input("Enter a new number: "))
   else:
    print("Your guess is too high")

    print()
    guess = int(input("Enter a new number: "))

  print("Congrats! The number was:", +str(secretNumber))

if __name__=="__main__":
  main()
