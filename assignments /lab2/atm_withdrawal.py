
balance = float(input("Enter your balance: "))
withdraw_amount = float(input("Enter amount to withdraw: "))

if withdraw_amount % 100 == 0 and withdraw_amount <= balance and (balance - withdraw_amount) >= 500:
    print("withdrawal successful.")
else:
    print("withdrawal failed.")