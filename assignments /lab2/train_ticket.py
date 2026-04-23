
age = int(input("Enter your age: "))

if age < 5:
    print("Ticket is Free")
elif 5 <= age <= 17:
    print("Ticket price: ₹100")
elif 18 <= age <= 59:
    print("Ticket price: ₹200")
else:
    print("Ticket price: ₹120")
