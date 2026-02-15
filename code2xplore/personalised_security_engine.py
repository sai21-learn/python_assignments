scores = [10, 45, 78, 120, -5, 30, 99, 150]
register_number = int(input("Enter your register number: "))
D = register_number % 10
print("Register Digit (D):", D)

low_risk = []
medium_risk = []
high_risk = []
critical_risk = []

total_valid = 0
ignored_entries = 0

for score in scores:
    if score < 0:
        ignored_entries = ignored_entries + 1
    else:
        total_valid = total_valid + 1
        if score <= 30:
            low_risk.append(score)
        elif score <= 60:
            medium_risk.append(score)
        elif score <= 100:
            high_risk.append(score)
        else:
            critical_risk.append(score)

print("\n--- Categorized Data Before Filtering ---")
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)

removed_due_to_personalization = 0

if D % 2 == 0:
    removed_due_to_personalization = len(low_risk)
    low_risk = []

else:
    removed_due_to_personalization = len(critical_risk)
    critical_risk = []
print("\n--- After Personalized Filtering ---")
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)

print("\nTotal Valid Entries:", total_valid)
print("Ignored Entries:", ignored_entries)
print("Removed Due to Personalization:", removed_due_to_personalization)
