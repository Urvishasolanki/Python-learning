import random
otp=random.randrange(100000,1000000)
print(otp)
user=int(input("Enter OTP"))
if otp==user:
    print("ACCESS GRANTED!!!")
else:
    print("ACCESS DENIED!!!")