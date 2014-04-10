# Testing out a RPG sim

import random



def dice_roller(dice):
# generate random number 1 - dice(eg d6, d10, d12)
    dice = random.randint(1, dice)
    return dice

d4 = dice_roller(4)
d6 = dice_roller(6)
d10 = dice_roller(10)
d12 = dice_roller(12)
d20 = dice_roller(20)

two_d6 = dice_roller(6) + dice_roller(6)
two_d10 = dice_roller(10) + dice_roller(10)
two_d12 = dice_roller(12) + dice_roller(12)
two_d20  = dice_roller(20) + dice_roller(20)

print("Your lone hero is surrounded by a massive army of trolls.")
print("Their decaying green bodies stretch out, melting into the horizon.")
print("Your hero unsheathes his sword for the last fight of his life.\n")

health = 100
trolls = 0
#damage = dice_roller(4)

while health > 0:
    trolls += 1
    damage = dice_roller(12)
    health -= damage

    print("Your hero swings and defeats an evil troll, " \
          "but takes", damage, "damage points.\n")
    print("Current health: ", health)
print("Your hero fought valiantly and defeated", trolls, "trolls.")
print("But alas, your hero is no more.")

input("\n\nPress the enter key to exit.")
