
usage = int(input("Enter data usage in MB: "))

if usage < 1500:
    print("Status: Safe")
elif 1500 <= usage < 2048:
    print("Status: Warning")
elif usage >= 2048:
    print("Status: Extra charge ₹50")
