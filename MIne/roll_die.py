# This program will execute dice_type rolls by having the user
# input the number of dice to be rolled, and the type of dice
# to roll (example: 2 rolls of six-sided dice).

import random
import re

print("Welcome to AJ's Dice Roller 3000. \nWhen prompted type your desired roll (eg: 2d6)\n\n\n")

def program():
    times_to_roll, dice_type = input_taker()
    roller(times_to_roll, dice_type)
    print("\n\nYou got", str(random_number) + ".")
    input()
    program()

def input_taker():
    """Prompts the user to input how many times to roll"""

    dice = input("What roll? ")
    dice = dice.split('d')

    times_to_roll = int(dice[0])
    dice_type = int(dice[1])

    return times_to_roll, dice_type

def roller(times_to_roll, dice_type):
    """Takes the number of times to roll and the type of dice
    (d6, d12, etc.), executes the roll, and adds up the total."""

    i = 0
    global random_number
    random_number = 0
    while i != times_to_roll:
        random_number += random.randint(1, dice_type)
        i += 1
    return random_number


program()