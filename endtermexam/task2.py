data = [5,3,5,2,8,3,10,2]
unique=sorted(set(data))
transform = [x *2 for x in unique if x <=4 ]
transform.append(8)


result=[x **2 for x in transform ]
result.sort()
print(*result)
