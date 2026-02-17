full_name = None
age = None
email_id = None

temp_name = input (" FULL NAME : ")
if temp_name[0] == " " or temp_name[len(temp_name)-1]== " " :
    pass
else :
    if " " in temp_name :
        full_name = temp_name
temp_email = input ("EMAIL ID : ")
if "@" in temp_email and "." in temp_email :
    if temp_email[0]== "@":
        pass
    else :
        email_id = temp_email

temp_mobileno = input(" MOBILE NUMBER : ")
if len(temp_mobileno) == 10 :
    if  temp_mobileno[0] == 0 :
        pass
    else :
        if temp_mobileno.isdigit :
            mobile_no  = temp_mobileno
temp_age = int(input("AGE : "))
if 18 < temp_age < 60:
    age = temp_age
if full_name is not None and age is not None and email_id is not None:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")

