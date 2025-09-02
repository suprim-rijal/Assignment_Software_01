#Task2

import random as rd

def diceRoller(number):
    return rd.randint(1,number)

userInput = int(input("Enter a number of side role playing dice do you want?:"))

while True:
    rollDice = diceRoller(userInput)
    if rollDice == userInput:
        print(f"You rolled a {userInput}!, Exiting the Program...")
        break
    else:
        print(f"You rolled a {rollDice}")