def func1():
 try:
    l=[1,5,6,7]
    i=int(input("enter the index:"))
    print(l[i])
    return 1
 except:
    print("some error occured")
    return 0
 print("i am always executed")
# not always printed because of it is in the function
x=func1()
print(x)