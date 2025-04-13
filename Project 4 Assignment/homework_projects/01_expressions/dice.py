# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

dice_side=6

def main():
    dice1:int=random.randint(1,dice_side)
    dice2:int=random.randint(1,dice_side)

    total:int=dice1+dice2

    print(f"Dice have {dice_side} sides each")
    print(f"First Die : {dice1}")
    print(f"Second Die : {dice2}")
    print(f"Total of two dice : {total}")
main()