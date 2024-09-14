x=10
print(x)
def my_func():
    global x
    x=5
    y=2
    print(y)
my_func()
print(x)
#chnage global variable inside function