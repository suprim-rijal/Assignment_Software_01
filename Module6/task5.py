#Task5

def evenList(myList):
    for num in myList:
        if num%2 ==0:
            cutdownList.append(num)
        else:
            continue
    return cutdownList

cutdownList = []
originaList = []
usrList = int(input("How many element do you want in the list? "))
for number in range(usrList):
    elements = int(input(f"Enter element number {number+1} : "))
    originaList.append(elements)

print(f"The original list is {originaList}")
print(f"The cut down list is {evenList(originaList)}")