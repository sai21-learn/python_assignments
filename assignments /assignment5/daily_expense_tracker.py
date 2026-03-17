expenses = []

print("Enter your expenses (type 'done' to finish):")

while True:
    entry = input("Expense amount: ")

    if entry.lower() == 'done':
        break
    try:
        amount = float(entry)
        expenses.append(amount)
    except ValueError:
        print("Please enter a valid number.")

print("\nDaily Expenses:")
for x in expenses:
    print(f"- {x:.2f} rs")

total = sum(expenses)
print(f"Total Expense: {total:.2f} rs")