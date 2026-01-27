unit=int(input("Enter a unit"))
if unit < 100:
    bill=50+1.5*unit
    print("amount to paid $",bill)
elif unit >= 100 and unit < 200:
    bill=50+2.5*unit
    print("amount to paid",bill)
elif unit >= 200 and unit < 300:
    bill=50+3.5*unit
    print("amount to paid",bill)
elif unit >= 300:
    bill=50+6*unit
    print("amount to paid",bill)
else:
    print("Invalid input")

