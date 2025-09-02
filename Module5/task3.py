#Task3
isprime = True
userInput = int(input("Enter a number to check: "))
if userInput < 0:
    print("Please enter a positive integer to check.")
elif userInput == 0 or userInput == 1:
    print(f"{userInput} is neither prime nor composite.")
else:
    for i in range(2,userInput):
        if userInput % i == 0:
            isprime = False
            break
    if isprime:
        print(f"{userInput} is a prime number.")
    else:
        print(f"{userInput} is a composite number.")
