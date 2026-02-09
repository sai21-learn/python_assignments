roll = int(input("Enter number of elements : "))

roll_numbers = [0] * roll

for i in range(roll):
    roll_numbers[i]=int(input("enter roll numbers : "))
    print(i,roll_numbers)

print("Total elements:", roll)



