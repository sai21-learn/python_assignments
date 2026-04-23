
row = int(input("Enter seat row number: "))

if 1 <= row <= 5:
    print("Price: ₹250")
elif 6 <= row <= 10:
    print("Price: ₹200")
elif 11 <= row <= 15:
    print("Price: ₹150")
else:
    print("Invalid row number")
