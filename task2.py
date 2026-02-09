percentages = [70,95,80,65,40]
eligible = 0
for i in percentages :
    if i>=75 :
        eligible +=1
        print ("Eligible " , i )
    elif i<75 and i>60 :
        print ("Condemtion",i)
    else :
        print ("Not Eligible " , i)
print ("Total Eligible Students :" , eligible)