# Day 5: Emergency Resource Dispatch Analyzer

## Challenge Description
Analyze emergency resource requests by categorizing demand levels (No Demand: 0, Low: 1-20, Moderate: 21-50, High: >50). Apply personalized filtering based on name length PLI = L % 3 to remove specific demand categories based on the PLI value.

## Approach / Logic Used
- Calculate PLI from name length without spaces: PLI = L % 3
- Categorize requests into four demand buckets (No Demand, Low, Moderate, High) and invalid requests
- Filter categories based on PLI value:
  - PLI 0: removes Low Demand only
  - PLI 1: removes High Demand only
  - PLI 2: removes Low, High, and No Demand (keeps only Moderate)
- Provide allocation report with categorization and removal count

## Personalized Length Index (PLI) - Explained

1. Take the full name provided
2. Count all letters (ignore spaces): L = total letter count
3. Calculate PLI = L % 3 (modulo 3)
   - If PLI = 0 → remove Low Demand requests
   - If PLI = 1 → remove High Demand requests
   - If PLI = 2 → remove Low Demand, No Demand, and High Demand requests (keep only Moderate)

**Example:** "Alice Brown" has 10 letters → PLI = 10 % 3 = 1 → High Demand items get filtered out

## Algorithm / Steps
1. Input full name and resource requests
2. Calculate L = name length without spaces, PLI = L % 3
3. Categorize requests into:
   - No Demand (0)
   - Low Demand (1-20)
   - Moderate Demand (21-50)
   - High Demand (>50)
   - Invalid Requests (negative values)
4. Apply PLI-based filtering:
   - PLI = 0: Remove Low Demand requests
   - PLI = 1: Remove High Demand requests
   - PLI = 2: Remove Low Demand, High Demand, and No Demand requests
5. Display allocation report with filtered results and removal count

## Sample Test Cases

### Test Case 1: PLI = 1 (Remove Low Demand)
**Input:**
```
Enter your full name: Arun Kumar
Enter resource requests separated by spaces: 10 25 60 -5 0 18
```
**Output:**
```
Full Name Length (L): 10
PLI Value: 1
Total Valid Requests: 4
Requests Removed Due to PLI: 2
Low Demand: []
Moderate Demand: [25]
High Demand: [60]
No Demand: [0]
Invalid Requests: [-5]
```

### Test Case 2: PLI = 1 (Remove Low Demand)
**Input:**
```
Enter your full name: Riya
Enter resource requests separated by spaces: 5 22 55 100 -3 1
```
**Output:**
```
Full Name Length (L): 4
PLI Value: 1
Total Valid Requests: 5
Requests Removed Due to PLI: 2
Low Demand: []
Moderate Demand: [22]
High Demand: [55, 100]
No Demand: []
Invalid Requests: [-3]
```

### Test Case 3: PLI = 2 (Remove High Demand)
**Input:**
```
Enter your full name: Karan Singh
Enter resource requests separated by spaces: 2 45 75 19 0 -8 51
```
**Output:**
```
Full Name Length (L): 11
PLI Value: 2
Total Valid Requests: 5
Requests Removed Due to PLI: 2
Low Demand: [2, 19]
Moderate Demand: [45]
High Demand: []
No Demand: [0]
Invalid Requests: [-8]
```
