#Task3

storage={}

print("Menu:-")
print("1.Enter new airport information")
print("2.Fetch airport information")
print("3.Quit the program")

while True:
  choice = int(input("Enter the options between 1 to 3: "))

  if choice == 1:
     airport_Name = input("Enter airport name:")
     icao_Code = input("Enter ICAO code of airport:")
     storage[icao_Code] = airport_Name
     print("Data Added Sucessfully.")

  elif choice == 2:
     icao_Code = input("Enter ICAO code of airport:")
     if icao_Code in storage:
         print(f"The aiport name is {storage[icao_Code]}") 
     else:
        print(f"No data on the given: {icao_Code} ICAO code.")

  elif choice == 3:
     print("Quitting the program....")
     break
  else:
     print("Invalid Choice !!!")

print(storage)