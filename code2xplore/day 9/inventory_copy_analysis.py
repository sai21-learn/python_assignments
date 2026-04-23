import copy
import json

roll_number = 24110011531
def create_inventory():
    return [
        {"item": "Laptop", "details": {"price": 50000, "stock": 10, "supplier_rating": 4.5}},
        {"item": "Phone", "details": {"price": 20000, "stock": 25, "supplier_rating": 4.2}},
        {"item": "Tablet", "details": {"price": 15000, "stock": 15, "supplier_rating": 4.0}}
    ]
def apply_discount(data):
    target = roll_number % len(data)
    for i in range(len(data)):
        if i == target:
            data[i]["details"]["price"] = int(data[i]["details"]["price"] * 0.90)
            data[i]["details"]["stock"] -= 5
            data[i]["item"] = data[i]["item"] + " (Discounted)"
def compare_data(original, modified):
    changed = 0
    unchanged = 0
    differences = []
    
    for i in range(len(original)):
        if original[i] != modified[i]:
            changed += 1
            differences.append(f"Item {i} changed! Original: {original[i]}, Modified: {modified[i]}")
        else:
            unchanged += 1
            
    return differences, (changed, unchanged)
baseline = create_inventory()

# Shallow copy test
print("--- Shallow Copy ---")
orig_shallow = create_inventory()
shallow_copy = copy.copy(orig_shallow)
apply_discount(shallow_copy)

print("Original Inventory:")
print(json.dumps(orig_shallow, indent=2))
print("Shallow Copy Result:")
print(json.dumps(shallow_copy, indent=2))

diffs_s, summary_s = compare_data(baseline, orig_shallow)
print("Differences:")
for d in diffs_s:
    print(d)
print("Tuple Summary:", summary_s)

print("\n--- Deep Copy ---")
orig_deep = create_inventory()
deep_copy = copy.deepcopy(orig_deep)
apply_discount(deep_copy)

print("Original Inventory:")
print(json.dumps(orig_deep, indent=2))
print("Deep Copy Result:")
print(json.dumps(deep_copy, indent=2))

diffs_d, summary_d = compare_data(baseline, orig_deep)
print("Differences:")
if not diffs_d:
    print("No changes in original data.")
for d in diffs_d:
    print(d)
print("Tuple Summary:", summary_d)

print("\n--- Explanation ---")
print("Shallow copy failed because it only copies the outer list.")
print("The nested 'details' dictionaries are still shared in memory between the original and the copy.")