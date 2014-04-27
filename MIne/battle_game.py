# Testing out a RPG sim

import random



def dice_roller(dice):
# generate random number 1 - dice(eg d6, d10, d12)
    dice = random.randint(1, dice)
    return dice

print("Your lone hero is surrounded by a massive army of trolls.")
print("Their decaying green bodies stretch out, melting into the horizon.")
print("Your hero unsheathes his sword for the last fight of his life.\n")

health = 100
trolls = 0
#damage = dice_roller(4)
total_damage = 0
print("Starting health", health)

while health > 0:
    trolls += 1
    roll = random.randint(0,22)
    if roll == 0:
        print("The troll misses! Your hero defeats him without a scratch!")
        print
        print("Current health: ", health)
        print("\n")
    else:
        damage = dice_roller(roll)
        total_damage = damage + total_damage
        health -= damage

        print("Your hero swings and defeats an evil troll, " \
          "but takes", damage, "damage points.")
        print("Current health: ", health)
        print("\n")

print("Your hero fought valiantly and defeated", trolls, "trolls.")
print("But alas, your hero is no more.")
print("He took",total_damage, "damage before he succumbed.")
# input("\n\nPress the enter key to exit.")
