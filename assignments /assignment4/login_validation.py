username = input("Enter Username ")
if not username :
    print( " Username can't be empty . Try again ")
else :
    password = input(" Enter passoword : ")
    if len(password) < 8 :
        print(" Passsword can't be less than 8 charectors ,  try again !!")
    else :
        print(" Login successful")
