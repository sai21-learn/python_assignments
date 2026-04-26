# Day 9: Inventory Data Corruption Simulator (Shallow vs Deep Copy)

## Challenge Description
A warehouse system maintains inventory where each product contains nested details (price, stock, supplier info). The system must analyze how data changes when copied and modified — simulating real-world data corruption issues. The program creates both shallow and deep copies of the inventory, modifies them based on a custom rule, and compares the structures to detect if the original data was corrupted.

## Approach / Logic Used
- Store the initial inventory as a list of dictionaries containing nested details (like price, stock, and supplier rating).
- Create a **shallow copy** of the inventory and apply mutation logic (price discount and stock reduction) to specific items based on a custom roll number rule.
- Create a **deep copy** of the inventory and apply the exact same mutation logic.
- Compare the original baseline data against the mutated states to detect any data corruption.
- Summarize the analysis in a tuple showing `(changed_items_count, unchanged_items_count)`.
- Provide a clear explanation of why the shallow copy fails to isolate the nested modifications.

## Algorithm / Steps
1. Initialize the baseline inventory data with items and their nested details (price, stock, supplier rating).
2. Generate a **shallow copy** using `copy.copy()`.
3. Apply the custom mutation to the shallow copy where the index matches `roll_number % length` (reduces nested price by 10% and stock by 5).
4. Compare the baseline inventory with the original inventory object to observe that the nested original data was unintentionally corrupted.
5. Generate a **deep copy** using `copy.deepcopy()`.
6. Apply the same custom mutation to the deep copy.
7. Compare the baseline inventory with the original inventory object to observe that the original data remained completely independent and safe.
8. Output the detailed JSON representations, differences observed, and tuple summaries for both scenarios.
9. Display a compulsory explanation explaining the memory reference differences between shallow and deep copies.

## Programming Concepts Used
- **Lists and Dictionaries**: To store the structured nested inventory data.
- **Nested Data Structures**: Managing dictionaries inside lists of dictionaries.
- **Functions**: Encapsulating creation, mutation, and comparison logic (`create_inventory`, `apply_discount`, `compare_data`).
- **Loops (for)**: Iterating over inventory items to apply changes and compare states.
- **Conditions (if/else)**: Applying custom logic based on index matching and detecting differences.
- **Shallow Copy (`copy.copy()`)**: Creating a copy with shared nested references.
- **Deep Copy (`copy.deepcopy()`)**: Creating an entirely independent clone of the data in memory.
- **Tuples**: Returning and displaying a summary of changed vs. unchanged counts.

## Key Learning Points
- **Memory References**: Understanding how Python handles object references in memory.
- **Shallow vs Deep Copy**: Seeing first-hand why shallow copies fail to isolate nested data modifications, while deep copies safely clone the entire nested structure.
- **Data Isolation**: Learning how to prevent accidental real-world data corruption when dealing with complex, nested data formats (like JSON).
- **State Comparison**: Writing logic to analyze and report the differences between a baseline state and a potentially corrupted state.
