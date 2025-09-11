#Task1

season = ('spring', 'summer', 'autumn', 'winter')
userInput = int(input("Enter the number of month (1-12): "))

winter = (12,1,2)
spring = (3,4,5)
summer = (6,7,8)
autumn = (9,10,11)

if userInput in winter:
    print("The crossponding Season is Winter.")
elif userInput in spring:
    print("The crossponding Season is Spring.")
elif userInput in summer:
    print("The crossponding Season is Summer.")
elif userInput in autumn:
    print("The crossponding Season is Autumn.")
else:
    print(f"{userInput} is Invalid!!! number of month.")