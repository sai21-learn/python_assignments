marks = [90,56,78,98,24,10,45]
valid_students = len(marks)
total_failed_students = 0
print("STUDENTS GRADES")
for i in range (len(marks)) :
    if 100 > marks[i] >90 :
        print(marks[i]," -> Excellent ")
    elif 89 > marks[i] > 75 :
        print (marks[i] ," -> Very Good  ")
    elif 74 >marks[i]>60 :
        print(marks[i]," -> Good ")
    elif 59 > marks[i] > 40 :
        print(marks[i]," -> Average  ")
    elif 100 < i and i< 0 :
        print(marks[i] , "-> INVALID")
        valid_students = valid_students -1
    else :
        print(marks[i] , "-> Fail ")
        total_failed_students = total_failed_students + 1

print("-- SUMMARY --")
print(" TOTAL Valid Students : ",valid_students)
print(" Total failed Students : ",total_failed_students)