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

### Test Case 1: PLI = 0 (Remove Low Demand)
**Input:**
```
Name: Alice Brown (L=10, PLI=1)
Requests: 12, 45, 75, 8, 52
```
**Output:**
```
Low Demand: [], Moderate Demand: [45], High Demand: [75, 52], No Demand: []
Removed: 2
```

### Test Case 2: PLI = 1 (Remove High Demand)
**Input:**
```
Name: John Smith (L=9, PLI=0)
Requests: 10, 25, 35, 60, 15
```
**Output:**
```
Low Demand: [10, 15], Moderate Demand: [25, 35], High Demand: [], No Demand: []
Removed: 1
```

### Test Case 3: PLI = 2 (Remove Low, High, and No Demand)
**Input:**
```
Name: Bob Wilson (L=9, PLI=0)
Requests: 5, -10, 30, 100, 0, 15, 55
```
**Output:**
```
Low Demand: [], Moderate Demand: [30], High Demand: [], No Demand: [], Invalid Requests: [-10]
Removed: 4
```
