#Task3

gender = input("Enter the gender (M or F): ")
hamoglobinLevel = float(input("Enter the hemoglobin level (g/l): "))   

if gender == "M":
    if hamoglobinLevel < 134:
        print("Your hemoglobin level is low.")
    elif 134 <= hamoglobinLevel <= 167:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high.")
elif gender == "F":
    if hamoglobinLevel < 117:
        print("Your hemoglobin level is low.")
    elif 117 <= hamoglobinLevel <= 155:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high.")
else:
    print("Invalid character !!")