name = input("Enter your name: ")
password = input("Enter your password: ")

if name == "hema":
    if password == "456789":
        print("Login successful")
    else:
        print("Password is wrong")
else:
    print("Username is wrong")
