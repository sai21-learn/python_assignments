
units = int(input("Enter number of units: "))
bill = 0

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + ((units - 100) * 3)
elif units <= 300:
    bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)
else:
    bill = (100 * 2) + (100 * 3) + (100 * 5) + ((units - 300) * 8)

print(f"Your electricity bill is: ₹{bill}")
