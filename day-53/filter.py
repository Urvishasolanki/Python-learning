l=[1,2,3,4,5,6]
def fil_fun(a):
    return a>2
l2=list(filter(fil_fun,l))
print(l2)