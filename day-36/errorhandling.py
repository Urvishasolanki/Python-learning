


a=input("enter number")
print(f"multiplication table of {a} is:")
try:
 for i in range(1,11):
    print(f"{int(a)} X {int(i)}={int(a)*(i)}")
except Exception as e:
 print(e)
print("some imp lines of code")
print("end of program")