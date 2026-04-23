# Day 8: Student Performance Analyzer

## Challenge Description
A university system needs to analyze student performance data to identify at-risk students, classify performance levels, and detect patterns in academic metrics. Generate synthetic student data including marks, attendance, and assignments, then perform comprehensive analysis including classification, statistical calculations, and pattern detection to provide insights for academic intervention.

## Approach / Logic Used
- Generate synthetic student data with random marks (0-100), attendance (0-100), and assignments (0-50)
- Calculate Performance Index (PI) using weighted formula: (marks * 0.6 + assignment * 0.4) * log(attendance + 1)
- Classify students into categories based on marks and attendance thresholds
- Perform statistical analysis including mean, median, standard deviation, and correlation
- Detect patterns: consistency (low std dev), attendance risk (many low attendance), high achievement (multiple top performers)
- Determine final system status based on detected patterns

## Student Classification Rules
| Marks | Attendance | Category |
|-------|------------|----------|
| < 40 | Any | At Risk |
| Any | < 50 | At Risk |
| 40–70 | ≥ 50 | Average |
| 71–90 | ≥ 50 | Good |
| > 90 | > 80 | Top Performer |

## Algorithm / Steps
1. Get last digit of roll number from user (0-9, 0 becomes 10)
2. Generate data for 10 students with random marks, attendance, assignments
3. Calculate Performance Index for each student
4. Create DataFrame and filter based on roll number (first N students)
5. Classify all students into categories using marks and attendance criteria
6. Perform statistical analysis on filtered data:
   - Calculate mean, median, standard deviation using NumPy
   - Compute manual mean for verification
   - Calculate correlation between marks and attendance
   - Normalize marks data
7. Detect patterns:
   - Consistency: Standard deviation < 15
   - Attendance Risk: More than 3 students with attendance < 50
   - High Achievement: 2 or more Top Performers
8. Determine final result based on patterns:
   - Stable Academic System: Consistency + High Achievement
   - Critical Attention Required: Attendance Risk present
   - Moderate Performance: Otherwise
9. Display filtered student data, categories, statistics, and final assessment
10. Generate histogram visualization of marks distribution

## Programming Concepts Used
- **Lists and Tuples**: Store student data and results
- **Loops (for)**: Data generation, classification, manual calculations
- **Conditions (if/elif/else)**: Student categorization and pattern detection
- **Functions**: Modular code organization (generate_data, classify_students, analyze_data)
- **NumPy Arrays**: Statistical calculations and correlation
- **Pandas DataFrame**: Data manipulation and filtering
- **Matplotlib**: Data visualization (histogram)
- **Random Module**: Synthetic data generation
- **Math Module**: Performance Index calculation