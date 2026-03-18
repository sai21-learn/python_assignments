# Day 6: Smart Transaction Risk Detector
# A program to analyze transactions and detect fraud patterns


# Get transaction amounts from user
transaction_input = input("Enter transaction amounts separated by spaces: ")

# Convert input string into list of numbers
transactions = []
temp_number = ""

# Manual parsing of input string (no built-in functions)
for character in transaction_input:
    if character == " ":
        if temp_number != "":
            transactions.append(int(temp_number))
            temp_number = ""
    else:
        temp_number = temp_number + character

# Add the last number if exists
if temp_number != "":
    transactions.append(int(temp_number))
print("Transactions received:", transactions)

# Create dictionary to store categorized transactions
transaction_categories = {
    "normal": [],
    "large": [],
    "high_risk": [],
    "invalid": []
}

# Classify each transaction using loop and conditions
for amount in transactions:
    if amount <= 0:
        transaction_categories["invalid"].append(amount)
    elif amount >= 1 and amount <= 500:
        transaction_categories["normal"].append(amount)
    elif amount >= 501 and amount <= 2000:
        transaction_categories["large"].append(amount)
    elif amount > 2000:
        transaction_categories["high_risk"].append(amount)

# Display categorized transactions
print(" Categorized Transactions ")
print("Normal (1-500):", transaction_categories["normal"])
print("Large (501-2000):", transaction_categories["large"])
print("High Risk (>2000):", transaction_categories["high_risk"])
print("Invalid (<=0):", transaction_categories["invalid"])

# Calculate total transaction value manually (no sum function)
total_value = 0
for amount in transactions:
    total_value = total_value + amount

# Count number of transactions manually (no len function)
number_of_transactions = 0
for amount in transactions:
    number_of_transactions = number_of_transactions + 1

# Count number of valid transactions (excluding invalid)
valid_transactions = 0
for amount in transactions:
    if amount > 0:
        valid_transactions = valid_transactions + 1

print(" Transaction Summary")
print("Total number of transactions:", number_of_transactions)
print("Valid transactions:", valid_transactions)
print("Total transaction value: Rs.", total_value)
print()

# Pattern Detection - using conditions to identify suspicious patterns

# Pattern 1: Check if more than 5 transactions (Frequent Transactions)
frequent_transactions = False
if number_of_transactions > 5:
    frequent_transactions = True
    print(" Pattern Detected: Frequent Transactions (More than 5 transactions)")

# Pattern 2: Check if sum of transactions > 5000 (Large Spending)
large_spending = False
if total_value > 5000:
    large_spending = True
    print(" Pattern Detected: Large Spending (Total > 5000)")

# Pattern 3: Count high-risk transactions manually
high_risk_count = 0
for amount in transaction_categories["high_risk"]:
    high_risk_count = high_risk_count + 1

suspicious_pattern = False
if high_risk_count >= 3:
    suspicious_pattern = True
    print("Pattern Detected: Suspicious Pattern (3 or more high-risk transactions)")

# Determine Risk Classification
# Create tuple with pattern information
pattern_summary = (frequent_transactions, large_spending, suspicious_pattern)

# Count patterns using manual counting
pattern_count = 0
if frequent_transactions:
    pattern_count = pattern_count + 1
if large_spending:
    pattern_count = pattern_count + 1
if suspicious_pattern:
    pattern_count = pattern_count + 1

# Risk classification logic
risk_level = ""

if pattern_count == 0:
    risk_level = "Low Risk"
elif pattern_count == 1 or pattern_count == 2:
    risk_level = "Moderate Risk"
elif pattern_count >= 3:
    risk_level = "High Risk"

print(" Final Risk Report ")
print("Risk Classification:", risk_level)
print()
print("Pattern Details:")
print("  - Frequent Transactions:", frequent_transactions)
print("  - Large Spending:", large_spending)
print("  - Suspicious Pattern:", suspicious_pattern)
print("  - Total Patterns Detected:", pattern_count)


# Use list comprehension to create transaction summary (mandatory requirement)
# This creates a list of tuples with (category, count) format
category_summary = [(category, len(transaction_categories[category])) for category in transaction_categories]

print("--- Category Summary ---")
for category_name, count in category_summary:
    print(f"{category_name.capitalize()}: {count} transactions")


# Final recommendation
if risk_level == "Low Risk":
    print("Account Status: Safe - No suspicious activity detected")
elif risk_level == "Moderate Risk":
    print("Account Status: Monitor - Review recent transactions")
else:
    print("Account Status: Alert - Immediate action needed")
