#Task1
import random as rd
userInput = int(input("How many times do you wan to roll the dice?"))
sum_of_dice = 0
for i in range(userInput):
    diceRolled = rd.randint(1,6)
    sum_of_dice += diceRolled
print(f"Sum of all dice rolled: {sum_of_dice}")