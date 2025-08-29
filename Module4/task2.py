#Task2
check = True

while check:
    userinput = int(input("Enter a number in inches: "))
    if userinput <0:
        check = False
    else:
     print(f"{userinput} inches is equal to {userinput*2.54} centimeters.")
    
else:
    print("Negative number entered. Exiting the program.")    
