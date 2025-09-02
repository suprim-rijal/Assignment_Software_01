#Task6

import math as m
def pizzaPicker(diameter,price):
    area = m.pi * (diameter/200)**2
    return price/area

pizza1_diameter = float(input("Enter a diameter for first pizza(in centimeters):"))
pizza1_price = float(input("Enter a price for first pizza(in euros):"))

pizza2_diameter = float(input("Enter a diameter for second pizza(in centimeters):"))
pizza2_price = float(input("Enter a price for second pizza(in euros):"))

pizza1 = pizzaPicker(pizza1_diameter,pizza1_price)
pizza2 = pizzaPicker(pizza2_diameter,pizza2_price)

if pizza1 < pizza2:
    print(f"The pizza one provides the best value which is {pizza1:.2f} euro per meter square.")
elif pizza2 < pizza1:
    print(f"The pizza two provides the best value which is {pizza2:.2f} euro per meter square.")
else:
    print("Both pizza has same value for the money!!")