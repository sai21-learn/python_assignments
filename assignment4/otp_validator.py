otp = input("Enter OTP: ")
if len(otp) != 6:
    print("Invalid OTP")
elif otp[0] < '0' or otp[0] > '9':
    print("Invalid OTP")
elif otp[1] < '0' or otp[1] > '9':
    print("Invalid OTP")
elif otp[2] < '0' or otp[2] > '9':
    print("Invalid OTP")
elif otp[3] < '0' or otp[3] > '9':
    print("Invalid OTP")
elif otp[4] < '0' or otp[4] > '9':
    print("Invalid OTP")
elif otp[5] < '0' or otp[5] > '9':
    print("Invalid OTP")

else:
    print("Valid OTP")
