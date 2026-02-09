marks = [35, 42, 50, 28, 40, 75]
print("Student results:")
for mark in marks:
    print(f"Mark: {mark}", end=" | ")
    if mark >= 40:
        print("Pass")
    else:
        print("Fail")
