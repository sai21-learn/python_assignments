
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))
bonus = 0

if years_of_service >= 10:
    bonus = 0.20 * salary
elif years_of_service >= 5:
    bonus = 0.10 * salary
elif years_of_service >= 2:
    bonus = 0.05 * salary

if bonus > 0:
    print(f"Your bonus is: ₹{bonus}")
else:
    print("No bonus")
