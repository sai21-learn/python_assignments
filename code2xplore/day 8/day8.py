import random
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# -------------------------------
# Function 1: Generate Data
# -------------------------------
def generate_data(n):

    students = [None] * n

    for i in range(n):
        sid = i + 1
        marks = random.randint(0, 100)
        attendance = random.randint(0, 100)
        assignment = random.randint(0, 50)

        # performance index
        pi = (marks * 0.6 + assignment * 0.4) * math.log(attendance + 1)

        students[i] = (sid, marks, attendance, assignment, pi)

    return students


# -------------------------------
# Function 2: Classification
# -------------------------------
def classify_students(data):

    categories = {
        "At Risk": [],
        "Average": [],
        "Good": [],
        "Top Performer": []
    }

    for i in range(len(data)):

        student = data[i]

        sid = student[0]
        marks = student[1]
        attendance = student[2]

        if marks < 40 or attendance < 50:
            categories["At Risk"] = categories["At Risk"] + [sid]

        elif marks >= 40 and marks <= 70:
            categories["Average"] = categories["Average"] + [sid]

        elif marks >= 71 and marks <= 90:
            categories["Good"] = categories["Good"] + [sid]

        elif marks > 90 and attendance > 80:
            categories["Top Performer"] = categories["Top Performer"] + [sid]

    return categories


# -------------------------------
# Function 3: Analysis
# -------------------------------
def analyze_data(df):

    marks = df["Marks"]

    mean_marks = np.mean(marks)
    median_marks = np.median(marks)
    std_dev = np.std(marks)

    # manual mean
    total = 0
    for m in marks:
        total = total + m
    manual_mean = total / len(marks)

    # correlation
    corr_matrix = np.corrcoef(df["Marks"], df["Attendance"])
    correlation = corr_matrix[0][1]

    # normalization
    min_m = min(marks)
    max_m = max(marks)

    normalized = [None] * len(marks)

    for i in range(len(marks)):
        normalized[i] = (marks[i] - min_m) / (max_m - min_m)

    df["Normalized"] = normalized

    return mean_marks, median_marks, std_dev, manual_mean, correlation


# -------------------------------
# MAIN PROGRAM
# -------------------------------

# input + validation
roll = int(input("Enter last digit of roll number: "))

if roll < 0 or roll > 9:
    print("Wrong number entered")
    exit()

# handle 0 case
if roll == 0:
    roll = 10

# always generate 10 students
n = 10

data = generate_data(n)

df = pd.DataFrame(data, columns=["ID", "Marks", "Attendance", "Assignment", "PI"])

# filter based on roll number
df_output = df.head(roll)

categories = classify_students(data)

# analysis on filtered data
mean_marks, median_marks, std_dev, manual_mean, correlation = analyze_data(df_output)


# pattern detection
if std_dev < 15:
    consistency = True
else:
    consistency = False

low_att = 0
for a in df_output["Attendance"]:
    if a < 50:
        low_att = low_att + 1

if low_att > 3:
    attendance_risk = True
else:
    attendance_risk = False

top = len(categories["Top Performer"])

if top >= 2:
    high_achievement = True
else:
    high_achievement = False


# final result
if consistency and high_achievement:
    result = "Stable Academic System"
elif attendance_risk:
    result = "Critical Attention Required"
else:
    result = "Moderate Performance"


# tuple output
summary = (mean_marks, std_dev, max(df_output["Marks"]))


# -------------------------------
# OUTPUT
# -------------------------------
print("\nStudent Data (Filtered):")
print(df_output)

print("\nCategories (All Students):")
print(categories)

print("\nStatistics:")
print("Mean:", mean_marks)
print("Manual Mean:", manual_mean)
print("Median:", median_marks)
print("Std Dev:", std_dev)
print("Correlation:", correlation)

print("\nTuple:")
print(summary)

print("\nFinal Result:")
print(result)


# -------------------------------
# GRAPH (Marks Distribution)
# -------------------------------
bins = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(df_output["Marks"], bins=bins)

plt.title("Marks Distribution (Filtered Students)")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")

plt.xticks(bins)

plt.show()
