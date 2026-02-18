full_name = input("Enter your full name: ")
user_input = input("Enter resource requests separated by spaces: ")
requests = []
values = user_input.split()

for v in values:
    requests.append(int(v))

name_no_spaces = ""
for ch in full_name:
    if ch != " ":
        name_no_spaces = name_no_spaces + ch

L = 0
for ch in name_no_spaces:
    L = L + 1

PLI = L % 2

low_demand = []
moderate_demand = []
high_demand = []
no_demand = []

invalid_requests = []

total_valid = 0

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
removed_count = 0

if PLI == 0:
    for value in low_demand:
        removed_count = removed_count + 1
    low_demand = []

elif PLI == 1:
    for value in high_demand:
        removed_count = removed_count + 1
    high_demand = []

elif PLI == 2:
    for value in low_demand:
        removed_count = removed_count + 1

    for value in high_demand:
        removed_count = removed_count + 1

    for value in no_demand:
        removed_count = removed_count + 1
    low_demand = []
    high_demand = []
    no_demand = []

print("Full Name Length (L):", L)
print("PLI Value:", PLI)
print("Total Valid Requests:", total_valid)
print("Requests Removed Due to PLI:", removed_count)

print("Low Demand:", low_demand)
print("Moderate Demand:", moderate_demand)
print("High Demand:", high_demand)
print("No Demand:", no_demand)
print("Invalid Requests:", invalid_requests)
