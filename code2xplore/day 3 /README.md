# Day 3: Student Performance Analyzer

## Challenge Description
Analyze student marks by section (I or J). Section I adds 1 point, Section J subtracts 1 point. Grade students (Excellent/Very Good/Good/Average/Fail) and report total students and failures.

## Approach / Logic Used
- Apply section-based mark adjustment (I: +1, J: -1)
- Grade based on ranges: 90-100 (Excellent), 75-89 (Very Good), 60-74 (Good), 40-59 (Average), <40 (Fail)
- Count and report total valid students and failed students

## Algorithm / Steps
1. Input section (I/J) and number of students N
2. Input marks for all N students
3. Apply section adjustment: add 1 for Section I, subtract 1 for Section J
4. Grade each student and display grades
5. Count failures and display summary

## Sample Test Cases

### Test Case 1: Section I
**Input:**
```
Section: i, Students: 3
Marks: 88, 75, 35
```
**Output:**
```
89 -> Excellent, 76 -> Very Good, 36 -> Fail
Total: 3, Failed: 1
```

### Test Case 2: Section J
**Input:**
```
Section: j, Students: 3
Marks: 95, 80, 65
```
**Output:**
```
94 -> Excellent, 79 -> Very Good, 64 -> Good
Total: 3, Failed: 0
```

### Test Case 3: All Failures
**Input:**
```
Section: j, Students: 2
Marks: 39, 20
```
**Output:**
```
38 -> Fail, 19 -> Fail
Total: 2, Failed: 2
```
