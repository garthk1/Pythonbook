import random

def program():
    dice = "3d12"
    times_to_roll, dice_type = input_taker(dice)
    roller(times_to_roll, dice_type)
    print(random_number)
def input_taker(dice):
    """Prompts the user to input how many times to roll"""
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