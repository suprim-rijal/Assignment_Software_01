#Task3

def conveter(userInput):
    return userInput * 3.78541

while True:
    number = float(input("Enter a number of Gallons to convert to Liters:"))
    if number < 0:
        print("Negative value entered. Exiting the Program...")
        break
    else:
        print(f"{number} gallons is {conveter(number):.3f} in liters")