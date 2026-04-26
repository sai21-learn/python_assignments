# Day 10: Student Data Drift Analyzer (Shallow vs Deep Copy with Statistical Analysis)

## Challenge Description
An educational institution maintains student records with multiple attributes (marks, attendance, nested scores). The system must detect data corruption when records are modified through shallow or deep copies, while also analyzing statistical drift in academic metrics. The program generates student data, applies mutations through both shallow and deep copies, and performs statistical analysis to classify the integrity of the data.

## Approach / Logic Used
- Generate a baseline set of student records containing nested details (marks, attendance, and scores array).
- Create a **shallow copy** and a **deep copy** of the student data independently.
- Apply custom mutation logic to both copies based on the roll number (e.g., increasing marks by square root, reducing attendance).
- Use **pandas DataFrames** to structure and compare the original and mutated datasets.
- Calculate statistical measures (mean, median, standard deviation) using **numpy** to detect data drift.
- Classify the results into categories: "Copy Failure Detected", "Stable Data", "Minor Drift", or "Critical Drift" based on threshold analysis.
- Compare the original data structures to detect if shallow copy corrupted the baseline (indicating copy failure).

## Algorithm / Steps
1. Initialize a baseline set of `n` student records with random marks (40-100), attendance (60-100), and two nested scores (10-25 each).
2. Create a **shallow copy** using `copy.copy()` of the original student list.
3. Create a **deep copy** using `copy.deepcopy()` of the original student list.
4. Create a **backup** (deep copy) of the original data to preserve the baseline for comparison.
5. Define a custom mutation rule based on `roll_no % 3 + 1` to determine the step size.
6. Apply mutations to both shallow and deep copies where index matches the step rule:
   - Increase marks by `sqrt(marks)`
   - Decrease attendance by 5
   - Increase first score by 5 and second score by 3
7. Convert all datasets (original, shallow copy, deep copy) into pandas DataFrames.
8. Calculate statistical metrics (mean, median, std, drift) comparing the backup with mutated versions using numpy.
9. Classify results based on whether shallow copy corrupted original data and the magnitude of drift.
10. Display comparison tables and statistical summaries for analysis.

## Programming Concepts Used
- **Lists and Dictionaries**: To store structured student records with multiple attributes.
- **Nested Data Structures**: Managing score arrays inside student dictionaries within a list.
- **Functions**: Encapsulating data generation, mutation, analysis, and classification logic.
- **Loops (for)**: Iterating over students to apply custom mutations based on index and roll number.
- **Conditions (if/else)**: Applying mutation logic conditionally and classifying results based on thresholds.
- **Shallow Copy (`copy.copy()`)**: Creating a list copy with shared nested dictionary references.
- **Deep Copy (`copy.deepcopy()`)**: Creating a completely independent clone of the entire data structure.
- **Pandas DataFrames**: Converting and comparing complex data structures in tabular format.
- **NumPy Arrays**: Computing statistical measures (mean, median, std, variance) on numeric columns.
- **Mathematical Functions**: Using `math.sqrt()` for custom mutation calculations.
- **Tuples**: Returning multiple values from analysis functions for comprehensive reporting.

## Key Learning Points
- **Memory References and Copy Types**: Understanding the critical difference between shallow and deep copies when dealing with nested data structures.
- **Data Corruption Detection**: Recognizing when modifications to a shallow copy inadvertently corrupt the original data through shared nested references.
- **Statistical Drift Analysis**: Detecting anomalies and changes in data through statistical measures rather than just raw value comparison.
- **Data Integrity Verification**: Comparing baseline and modified datasets to classify the severity of changes.
- **Data Science Libraries**: Leveraging pandas and numpy for robust data analysis and statistical computation.
- **Threshold-Based Classification**: Using configurable thresholds to categorize data states (stable, minor drift, critical drift).
