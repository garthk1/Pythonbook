# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random  

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("You have 10 chances to guess the correct number.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1
number_of_guesses = 1

# guessing loop
while number_of_guesses != 10:
    if guess > the_number:
        print("Lower...")
    elif guess < the_number:
        print("Higher...")
    else:
        print("\n\nYou guessed it!  The number was", the_number)
        print("And it only took you", tries, "tries!\n")
        exit()
    guess = int(input("Take a guess: "))
    tries += 1
    number_of_guesses +=1


print("\nI'm sorry. You did not guess the number correctly.")
print("\nThe number I chose was: ",the_number)
input("\n\nPress the enter key to exit.")
