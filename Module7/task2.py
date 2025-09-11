#Task2

print("Notice: Enter empty string or Press enter to Quit")

nameSet=set()

while True:
 userInput = str(input("Enter your name:"))
 if userInput == '':
     print("Null String entered!!! Loop Exited....")
     break
 else:
  nameSet.add(userInput)
 
if not nameSet:
  print("No names were entered...Set is Empty...")
else:
  print("Stored names are:")
  for names in nameSet:
   print(f"-{names}")

