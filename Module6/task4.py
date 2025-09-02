#Task4

def sumofList(myList):
    return sum(myList)

list = []
usrList = int(input("How many element do you want in the list? "))
for number in range(usrList):
    elements = int(input(f"Enter element number {number+1} : "))
    list.append(elements)

print(f"The sum of element from the list is {sumofList(list)}.")