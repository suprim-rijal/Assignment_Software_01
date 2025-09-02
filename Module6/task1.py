#Task1

import random as rd

def diceRoller():
    return rd.randint(1,6)

while True:
    rollDice = diceRoller()
    if rollDice == 6:
        print("You rolled a 6!, Exiting the Program")
        break
    else:
        print(f"You rolled a {rollDice}")
