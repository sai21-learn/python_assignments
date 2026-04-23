
nums = [10,3,5,10,2,3]
nums = list(set(nums))
for k in nums :
    print(k)
sums = 0
average= 0.00
squares=[]
cubes=[]
for y in range(len(nums)) :
    if nums[y] % 2 == 0 :
        nums[y]= nums[y]*nums[y]

    if nums[y] % 2 == 1 :
        nums[y]=nums[y]**3


maximum=nums[0]
minimum=nums[0]
for t in nums :
    sums=sums+t
    if maximum < t :
        maximum=t
    if minimum >t :
        minimum=t

average= sums/len(nums)
for z in nums :
    print(z)
print ("maximum :",maximum)
print("minimum :",minimum)
print("average :",average)
