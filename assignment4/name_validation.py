name = input("Enter full name: ")
if name[0] == ' ' or name[len(name) - 1] == ' ':
    print("Invalid Name")
elif ' ' in name:
    print("Valid Name")
else:
    print("Invalid Name")
