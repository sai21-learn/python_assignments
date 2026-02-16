# Input list (you can modify this)
requests = [10, 25, 60, -3, 0, 45, 80]

# Full name (enter your full name here)
full_name = "Sooraj"

# Remove spaces and calculate L
name_no_spaces = ""
for ch in full_name:
    if ch != " ":
        name_no_spaces = name_no_spaces + ch

L = 0
for ch in name_no_spaces:
    L = L + 1

PLI = L % 2

# Create required lists
low_demand = []
moderate_demand = []
high_demand = []
invalid_requests = []

total_valid = 0

# Categorization using for loop
for value in requests:

    if value < 0:
        invalid_requests.append(value)

    elif value == 0:
        pass

    elif value >= 1 and value <= 20:
        low_demand.append(value)
        total_valid = total_valid + 1

    elif value >= 21 and value <= 50:
        moderate_demand.append(value)
        total_valid = total_valid + 1

    elif value > 50:
        high_demand.append(value)
        total_valid = total_valid + 1


# Final Report
print("Full Name Length (L):", L)
print("PLI Value:", PLI)
print("Total Valid Requests:", total_valid)


print("Low Demand:", low_demand)
print("Moderate Demand:", moderate_demand)
print("High Demand:", high_demand)
print("Invalid Requests:", invalid_requests)
