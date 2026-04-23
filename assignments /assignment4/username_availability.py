username = input("Enter username: ")
if len(username) < 5:
    print("Not Available")
elif ' ' in username:
    print("Not Available")
else:
    print("Available")