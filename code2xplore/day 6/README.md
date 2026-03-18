# Day 6: Smart Transaction Risk Detector

## Challenge Description
A digital payment system records a sequence of transaction amounts made by a user in a day. The bank wants to automatically detect suspicious spending patterns to prevent fraud. Analyze the transactions and generate a detailed risk report with categorization and pattern detection.

## Approach / Logic Used
- Classify each transaction into categories: Invalid (≤0), Normal (1-500), Large (501-2000), or High Risk (>2000)
- Store categorized transactions in a dictionary
- Detect suspicious patterns:
  - Frequent Transactions: More than 5 transactions in a single day
  - Large Spending: Total transaction sum exceeds Rs. 5000
  - Suspicious Pattern: 3 or more high-risk transactions (>2000)
- Calculate risk level based on number of patterns detected:
  - Low Risk: 0 patterns detected
  - Moderate Risk: 1-2 patterns detected
  - High Risk: 3 or more patterns detected

## Transaction Classification Rules
| Amount | Category |
|--------|----------|
| ≤ 0 | Invalid Transaction |
| 1–500 | Normal |
| 501–2000 | Large |
| > 2000 | High Risk |

## Algorithm / Steps
1. Get transaction amounts from user (space-separated values)
2. Parse input string manually into a list of numbers (no built-in functions)
3. Classify each transaction into appropriate category using loops and conditions
4. Store all categorized transactions in a dictionary
5. Calculate:
   - Total transaction value (manual summation)
   - Number of valid/invalid transactions (manual counting)
6. Detect patterns:
   - Check if transaction count > 5 (Frequent Transactions)
   - Check if total value > 5000 (Large Spending)
   - Check if high-risk count >= 3 (Suspicious Pattern)
7. Count total patterns detected
8. Determine risk classification:
   - 0 patterns = Low Risk
   - 1-2 patterns = Moderate Risk
   - 3+ patterns = High Risk
9. Display categorized transactions, summary, patterns detected, and final risk assessment
10. Use list comprehension to create category summary

## Programming Concepts Used
- **Lists**: Store transactions and categorized amounts
- **Loops (for)**: Traverse list, count items, sum values, classify transactions
- **Conditions (if/elif/else)**: Classify transactions and detect patterns
- **Dictionary**: Store categorized transactions
- **Tuples**: Pattern summary (3-tuple with boolean values)
- **List Comprehension**: Create category summary [(category, count) for category]

## Sample Test Cases

### Test Case 1: Low Risk
**Input:**
```
Enter transaction amounts separated by spaces: 100 200 150 300 250
```
**Output:**
```
Transactions received: [100, 200, 150, 300, 250]

 Categorized Transactions 
Normal (1-500): [100, 200, 150, 300, 250]
Large (501-2000): []
High Risk (>2000): []
Invalid (<=0): []

Transaction Summary 
Total number of transactions: 5
Valid transactions: 5
Total transaction value: Rs. 1000

 Final Risk Report
Risk Classification: Low Risk

Pattern Details:
  - Frequent Transactions: False
  - Large Spending: False
  - Suspicious Pattern: False
  - Total Patterns Detected: 0

 Category Summary 
Normal: 5 transactions
Large: 0 transactions
High_risk: 0 transactions
Invalid: 0 transactions

✓ Account Status: Safe - No suspicious activity detected
```

### Test Case 2: Moderate Risk
**Input:**
```
Enter transaction amounts separated by spaces: 200 400 600 1500 800 2100 300 250
```
**Output:**
```
Transactions received: [200, 400, 600, 1500, 800, 2100, 300, 250]

 Categorized Transactions 
Normal (1-500): [200, 400, 300, 250]
Large (501-2000): [600, 1500, 800]
High Risk (>2000): [2100]
Invalid (<=0): []

 Transaction Summary 
Total number of transactions: 8
Valid transactions: 8
Total transaction value: Rs. 6850

  Pattern Detected: Frequent Transactions (More than 5 transactions)
 Pattern Detected: Large Spending (Total > 5000)

--- Final Risk Report ---
Risk Classification: Moderate Risk

Pattern Details:
  - Frequent Transactions: True
  - Large Spending: True
  - Suspicious Pattern: False
  - Total Patterns Detected: 2

Category Summary
Normal: 4 transactions
Large: 3 transactions
High_risk: 1 transactions
Invalid: 0 transactions

  Account Status: Monitor - Review recent transactions
```

### Test Case 3: High Risk
**Input:**
```
Enter transaction amounts separated by spaces: 2500 3000 2200 400 1800 100 2800
```
**Output:**
```
Transactions received: [2500, 3000, 2200, 400, 1800, 100, 2800]

Categorized Transactions 
Normal (1-500): [400, 100]
Large (501-2000): [1800]
High Risk (>2000): [2500, 3000, 2200, 2800]
Invalid (<=0): []

--- Transaction Summary ---
Total number of transactions: 7
Valid transactions: 7
Total transaction value: Rs. 14800

  Pattern Detected: Frequent Transactions (More than 5 transactions)
  Pattern Detected: Large Spending (Total > 5000)
  Pattern Detected: Suspicious Pattern (3 or more high-risk transactions)

--- Final Risk Report ---
Risk Classification: High Risk

Pattern Details:
  - Frequent Transactions: True
  - Large Spending: True
  - Suspicious Pattern: True
  - Total Patterns Detected: 3

--- Category Summary ---
Normal: 2 transactions
Large: 1 transactions
High_risk: 4 transactions
Invalid: 0 transactions

✗ Account Status: Alert - Immediate action needed
```

### Test Case 4: Handling Invalid Transactions
**Input:**
```
Enter transaction amounts separated by spaces: -100 0 500 2000 3000 -50
```
**Output:**
```
Transactions received: [-100, 0, 500, 2000, 3000, -50]

--- Categorized Transactions ---
Normal (1-500): [500]
Large (501-2000): [2000]
High Risk (>2000): [3000]
Invalid (<=0): [-100, 0, -50]

--- Transaction Summary ---
Total number of transactions: 6
Valid transactions: 3
Total transaction value: Rs. 5500

  Pattern Detected: Large Spending (Total > 5000)

--- Final Risk Report ---
Risk Classification: Moderate Risk

Pattern Details:
  - Frequent Transactions: False
  - Large Spending: True
  - Suspicious Pattern: False
  - Total Patterns Detected: 1

--- Category Summary ---
Normal: 1 transactions
Large: 1 transactions
High_risk: 1 transactions
Invalid: 3 transactions

  Account Status: Monitor - Review recent transactions
```

## Key Learning Points
- **Manual parsing**: Converting string input to numbers without using built-in functions like `split()`
- **Manual counting and summation**: Using loops instead of `len()` and `sum()`
- **Dictionary usage**: Organizing data by categories
- **Pattern detection**: Using multiple conditions to identify complex scenarios
- **List comprehension**: Creating concise lists from existing data
- **Tuple usage**: Storing related boolean values as a pattern summary
