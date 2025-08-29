array = []

while True:
    userinput = input("Enter a number (or press enter to exit): ")
    if userinput == "":   
        break
    num = int(userinput)
    array.append(num)   
    
if array:   
    print(f"Largest number is {max(array)}")
    print(f"Smallest number is {min(array)}")
else:
    print("No numbers were entered.")
