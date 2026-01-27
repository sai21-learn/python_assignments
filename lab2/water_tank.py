
level = int(input("Enter water level (%): "))

if 0 <= level <= 20:
    print("Status: Low")
elif 21 <= level <= 70:
    print("Status: Normal")
elif 71 <= level <= 100:
    print("Status: Full")
else:
    print("Invalid level")
