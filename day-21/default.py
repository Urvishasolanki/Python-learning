def average(a,b):
    print("the average is",(a+b)/2)
average(4,6)

#ignore default value 
def average(c=5,d=5):
     print("the average is",(c+d)/2)
average(3,3)

#take default value of c
def average(c=5,d=5):
     print("the average is",(c+d)/2)
average(3)

#take default value of b
def average(c=5,d=5):
     print("the average is",(c+d)/2)
average(d=6)


