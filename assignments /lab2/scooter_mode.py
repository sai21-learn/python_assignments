
battery = int(input("Enter battery percentage: "))

if battery > 70:
    print("Mode: Performance")
elif 30 <= battery <= 70:
    print("Mode: Normal")
else:
    print("Mode: Power Saving")
