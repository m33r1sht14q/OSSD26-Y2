print("----Password Authentication System----")

username = "Meer"
password = " A123456789c#"

attempts = 3

while True:
    user_name = input("Enter your username: ")
    user_password = input("Enter your password: ")

    if user_name == "" or user_password == "":
        print("Username and password cannot be empty, Try Again")
        continue

    if user_password == user_password and user_name == username:
        print("You enter correct password, You are logged in the portal")
        break

    else:
        attempts-=1
        if attempts > 0:
         print(f"You have {attempts} attempts remaining")
        else:
         print("You reached your limit your account is locked")
         break