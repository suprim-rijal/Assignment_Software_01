import random as rd
number=rd.randint(1,10)
guess=None
while guess!=number:
    guess=int(input("Guess a number between 1 and 10: "))
    if guess<number:
        print("Too low!")
    elif guess>number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the correct number.")