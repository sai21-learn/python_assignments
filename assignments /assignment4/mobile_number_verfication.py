mobile = input("Enter mobile number: ")

if len(mobile) != 10:
    print("Invalid Mobile Number")

elif mobile[0] < '0' or mobile[0] > '9':
    print("Invalid Mobile Number")
elif mobile[1] < '0' or mobile[1] > '9':
    print("Invalid Mobile Number")
elif mobile[2] < '0' or mobile[2] > '9':
    print("Invalid Mobile Number")
elif mobile[3] < '0' or mobile[3] > '9':
    print("Invalid Mobile Number")
elif mobile[4] < '0' or mobile[4] > '9':
    print("Invalid Mobile Number")
elif mobile[5] < '0' or mobile[5] > '9':
    print("Invalid Mobile Number")
elif mobile[6] < '0' or mobile[6] > '9':
    print("Invalid Mobile Number")
elif mobile[7] < '0' or mobile[7] > '9':
    print("Invalid Mobile Number")
elif mobile[8] < '0' or mobile[8] > '9':
    print("Invalid Mobile Number")
elif mobile[9] < '0' or mobile[9] > '9':
    print("Invalid Mobile Number")

else:
    print("Valid Mobile Number")
