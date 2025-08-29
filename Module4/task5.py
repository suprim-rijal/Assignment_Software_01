# Task5
username = "suprim"
password = "suprim123"
attempts = 5    
while attempts > 0:
    usernameinput = input("Enter your username: ")
    userpassword = input("Enter your password: ")
    if usernameinput == username and userpassword == password :
        print("Welcome!")
        break
    else:
        attempts -= 1
        print(f"Incorrect Credentials. You have {attempts} attempts left")
        if attempts == 0:
            print("Access denied.")


    
