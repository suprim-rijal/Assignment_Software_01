#Task1
lenght = int(input("Enter the lenght of the zander in centimeters: "))
sizeLimit = 42

if lenght < sizeLimit:
    print(f"Release the fish back into the lake. The zander is {sizeLimit - lenght} cm below the size limit.")
else:
    print("The zander meets the size limit.")
