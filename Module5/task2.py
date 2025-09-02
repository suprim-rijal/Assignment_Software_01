#Task2
array = []
check = True
while check:
    userInput = (input("Enter a number (string to stop the iteration): "))
    if userInput == "" or not userInput.lstrip('-').isdigit() :
     print("Exiting the program... ")
     check = False
    else:
        array.append(int(userInput))
        
array.sort(reverse=True)
last_five_digits = array[:5]
print("The last 5 largest digits in descending order are:")
for i in last_five_digits:
    print(i)

