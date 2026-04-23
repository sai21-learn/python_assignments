password = input("enter password :")
eval = 0
def check_password(password,eval):

    if len(password) > 8:
       eval = eval + 1
    if any(char.isdigit() for char in password):
        eval = eval + 1
    if any(char.isupper() for char in password):
        eval = eval + 1
    if any(char.islower() for char in password):
        eval = eval + 1
    if any(char in "!@#$%^&*(),.?:;{}|<> " for char in password):
        eval = eval + 1
    return eval

score = check_password(password,eval)
if score == 0 or score == 1 :
    print ("Weak")
if score == 2 or score == 3 :
    print (" Moderate ")
if score == 4 or score == 5 :
    print (" Strong ")

