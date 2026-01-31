student_id=input("Enter studentID : ").strip()
email= input("Enter EmailID : ").strip()
password= input("Enter Password : ").strip()
referral= input("Enter Referral Codes : ").strip()
valid = True
if not (
    len (student_id) == 7 and
    student_id[0:3] == "CSE" and
    student_id[3] == "-" and
    student_id[4].isdigit() and
    student_id[5].isdigit() and
    student_id[6].isdigit()
) :  valid = False
if not (
        "@" in email and
        "." in email and
        email [0]!="@" and
        email[-1]!= "@" and
        email.endswith(".edu")
) :
    valid = False
if not (
            len (password) >= 8 and
            password[0].isupper() and
             "0" in password or "1" in password or "2" in password or
             "3" in password or "4" in password or "5" in password or
             "6" in password or "7" in password or "8" in password or
             "9" in password
):
    valid = False
if not (
            len(referral)==6 and
            referral[0:3] == "REF" and
            referral[3].isdigit() and
            referral[4].isdigit() and
            referral[5] =="@"
    ):
    valid = False
if valid :  print("APPROVED")
else : print("REJECTED")
