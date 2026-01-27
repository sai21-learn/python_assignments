
speed = int(input("Enter your speed (km/h): "))

if speed <= 60:
    print("No fine")
elif 61 <= speed <= 80:
    print("Fine: ₹500")
elif 81 <= speed <= 100:
    print("Fine: ₹1000")
else:
    print("Fine: ₹2000 + license warning")
