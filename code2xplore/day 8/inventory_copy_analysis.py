import copy
import json

# Dummy roll number for the Custom Mutation Rule
ROLL_NUMBER = 42

def create_inventory():
    """
    Step 1: Create original inventory.
    Added 'supplier_rating' as an additional nested field as per requirements.
    """
    return [
        {
            "item": "Laptop",
            "details": {"price": 50000, "stock": 10, "supplier_rating": 4.5}
        },
        {
            "item": "Phone",
            "details": {"price": 20000, "stock": 25, "supplier_rating": 4.2}
        },
        {
            "item": "Tablet",
            "details": {"price": 15000, "stock": 15, "supplier_rating": 4.0}
        }
    ]

def apply_discount(data, roll_number):
    """
    Step 3: Mutation Logic
    Reduces price by 10% and modifies stock for a specific item.
    Target item is chosen based on the roll number rule.
    """
    length = len(data)
    target_index = roll_number % length
    
    for i in range(length):
        if i == target_index:
            # Modify nested data (price and stock)
            data[i]["details"]["price"] = int(data[i]["details"]["price"] * 0.90)
            data[i]["details"]["stock"] -= 5
            
            # Modify the outer level string
            data[i]["item"] = data[i]["item"] + " (Discounted)"

def compare_data(baseline, current):
    """
    Step 4: Analysis
    Compares the baseline (pure original state) with the current state.
    Returns a list of differences and a tuple (changed, unchanged).
    """
    changed_count = 0
    unchanged_count = 0
    differences = []
    
    for i in range(len(baseline)):
        if baseline[i] != current[i]:
            changed_count += 1
            diff_msg = (f"Item at index {i} was corrupted/modified in the original data.\n"
                        f"  Original intended state: {baseline[i]}\n"
                        f"  Current corrupted state: {current[i]}")
            differences.append(diff_msg)
        else:
            unchanged_count += 1
            
    return differences, (changed_count, unchanged_count)

def print_json(title, data):
    print(f"\n{title}:")
    print(json.dumps(data, indent=2))

def main():
    # We keep a pristine baseline to compare against and prove data corruption
    baseline_inventory = create_inventory()
    
    print("="*60)
    print(" SCENARIO A: SHALLOW COPY ANALYSIS")
    print("="*60)
    
    # Create inventory and a shallow copy
    original_inventory_A = create_inventory()
    shallow_copy = copy.copy(original_inventory_A)
    
    print(f"Applying discount to SHALLOW COPY (Roll Number {ROLL_NUMBER}, Target Index {ROLL_NUMBER % len(shallow_copy)})...")
    apply_discount(shallow_copy, ROLL_NUMBER)
    
    print_json("Original Inventory (After Shallow Copy Mutation)", original_inventory_A)
    print_json("Shallow Copy Result", shallow_copy)
    
    print("\n--- Differences Observed (Baseline vs Original A) ---")
    diffs_A, summary_A = compare_data(baseline_inventory, original_inventory_A)
    for d in diffs_A:
        print(d)
    print(f"\nTuple Summary -> (changed_items_count, unchanged_items_count): {summary_A}")
    
    
    print("\n" + "="*60)
    print(" SCENARIO B: DEEP COPY ANALYSIS")
    print("="*60)
    
    # Create inventory and a deep copy
    original_inventory_B = create_inventory()
    deep_copy = copy.deepcopy(original_inventory_B)
    
    print(f"Applying discount to DEEP COPY (Roll Number {ROLL_NUMBER}, Target Index {ROLL_NUMBER % len(deep_copy)})...")
    apply_discount(deep_copy, ROLL_NUMBER)
    
    print_json("Original Inventory (After Deep Copy Mutation)", original_inventory_B)
    print_json("Deep Copy Result", deep_copy)
    
    print("\n--- Differences Observed (Baseline vs Original B) ---")
    diffs_B, summary_B = compare_data(baseline_inventory, original_inventory_B)
    if not diffs_B:
        print("No differences found! The original data remained completely independent and safe.")
    for d in diffs_B:
        print(d)
    print(f"\nTuple Summary -> (changed_items_count, unchanged_items_count): {summary_B}")


    print("\n" + "="*60)
    print(" COMPULSORY EXPLANATION")
    print("="*60)
    print("Q: Why shallow copy failed to isolate changes?")
    print("A: When we use shallow copy (copy.copy()), Python creates a new outer list but populates it")
    print("   with references to the EXACT SAME nested dictionary objects from the original list in memory.")
    print("   When the mutation logic modifies the nested 'details' (price and stock) in the shallow copy,")
    print("   it is actually altering the shared dictionary object. This is evident in Scenario A's output,")
    print("   where the original inventory's nested details were unexpectedly corrupted, proving that the")
    print("   nested structures are not isolated.")
    print("   (Note: Reassigning strings like the 'item' key affects only the copy because strings are immutable).")
    print("\n   Conversely, deep copy (copy.deepcopy()) recursively duplicates all objects, including nested")
    print("   dictionaries, ensuring complete isolation and preventing data corruption as seen in Scenario B.")

if __name__ == "__main__":
    main()
