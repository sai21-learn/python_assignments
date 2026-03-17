marks = []
for i in range(5) :
    m=int (input("enter marks : "))
    marks.append(m)
    print (i , marks)
marks = [x + 5 for x in marks]
print (sum(marks ))