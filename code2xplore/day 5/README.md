# Day 5: Emergency Resource Dispatch Analyzer

## Challenge Description
Analyze emergency resource requests by categorizing demand levels (Low: 1-20, Moderate: 21-50, High: 50+). Apply personalized filtering based on name length PLI = L % 2 to remove Low Demand (if PLI even) or High Demand (if PLI odd).

## Approach / Logic Used
- Calculate PLI from name length (without spaces)
- Categorize requests into three demand buckets
- Filter categories based on PLI: remove Low if even, remove High if odd
- Provide allocation report with categorization and removal count

## Personalized Length Index (PLI) - Explained

1. Take the full name provided
2. Count all letters (ignore spaces): L = total letter count
3. Calculate PLI = L % 2 (modulo 2)
   - If L is even → PLI = 0 (remove High Demand requests)
   - If L is odd → PLI = 1 (remove Low Demand requests)

**Example:** "Alice Brown" has 10 letters → PLI = 10 % 2 = 0 (even) → High Demand items get filtered out

## Algorithm / Steps
1. Input full name and resource requests
2. Calculate L = name length without spaces, PLI = L % 2
3. Categorize requests into Low, Moderate, High, and Invalid (negative)
4. Display initial categorization
5. Apply PLI-based filtering
6. Display filtered results with removal count

## Sample Test Cases

### Test Case 1: Even PLI (Clear High Demand)
**Input:**
```
Name: Alice Brown (L=10, PLI=0)
Requests: 12, 45, 75, 8, 52
```
**Output:**
```
Low: [12, 8], Moderate: [45], High: []
Removed: 2
```

### Test Case 2: Odd PLI (Clear Low Demand)
**Input:**
```
Name: John Smith (L=9, PLI=1)
Requests: 10, 25, 35, 60, 15
```
**Output:**
```
Low: [], Moderate: [25, 35], High: [60]
Removed: 2
```

### Test Case 3: Mixed with Invalid
**Input:**
```
Name: Bob Wilson (L=9, PLI=1)
Requests: 5, -10, 30, 100, 0, 15, 55
```
**Output:**
```
Low: [], Moderate: [30], High: [100], Invalid: [-10]
Removed: 2
```
