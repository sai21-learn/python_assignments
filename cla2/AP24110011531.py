import math

nums = [4, 9, 16, 25, 36, 49, 64]

def fun1(nums):
    new_list = []
    for x in nums:
        if math.sqrt(x) % 2 != 1:
            new_list.append(x)
    return new_list

def fun2(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * math.sqrt(nums[i])
    return nums

def fun3(nums):
    return sorted(nums, key=lambda x: x % 10)

result = fun3(fun2(fun1(nums)))

for i in result:
    print(i)