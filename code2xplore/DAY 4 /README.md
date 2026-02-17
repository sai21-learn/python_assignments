# Day 4: Personalized Security Engine

## Challenge Description
Categorize vulnerability scores into risk levels (Low: 0-30, Medium: 31-60, High: 61-100, Critical: 100+). Apply personalized filtering based on register number's last digit D to remove Low Risk (if D even) or Critical Risk (if D odd).

## Approach / Logic Used
- Categorize scores into four risk buckets
- Calculate D = last digit of register number
- If D is even: remove all Low Risk entries
- If D is odd: remove all Critical Risk entries
- Display initial and filtered categorization with count of removed entries

## Algorithm / Steps
1. Input number of vulnerability scores and collect them
2. Input register number, extract last digit D
3. Categorize scores into four risk levels
4. Display initial categorization
5. Apply personalized filter based on D (even/odd)
6. Display filtered results and removal count

## Sample Test Cases

### Test Case 1: Even Register (Clear Low Risk)
**Input:**
```
Scores: 15, 45, 75, 120, -5
Register: 1234 (D=4)
```
**Output:**
```
Low Risk: [], Medium: [45], High: [75], Critical: [120]
Removed: 1
```

### Test Case 2: Odd Register (Clear Critical)
**Input:**
```
Scores: 20, 50, 90, 150
Register: 2345 (D=5)
```
**Output:**
```
Low Risk: [20], Medium: [50], High: [90], Critical: []
Removed: 1
```

### Test Case 3: Multiple Low Removals
**Input:**
```
Scores: 10, 25, 35, 55
Register: 5678 (D=8)
```
**Output:**
```
Low Risk: [], Medium: [35, 55], High: [], Critical: []
Removed: 2
```
