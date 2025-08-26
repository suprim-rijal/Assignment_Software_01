#Task2
 
cabinClass = input("Enter the cabin class (LUX, A, B, C): ")

if cabinClass == "LUX":
    print("Upper-deck cabin with a balcony.")

elif cabinClass == "A":
    print("Above the car deck, equipped with a window.")

elif cabinClass == "B":
    print("Windowless cabin above the car deck.")

elif cabinClass == "C":
    print("Windowless cabin below the car deck.")

else:
    print("Invalid cabin class !!")