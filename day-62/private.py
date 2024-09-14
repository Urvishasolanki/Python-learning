class emp:
    def __init__(self):
        self.__name="urvisha" #__ meas private

a=emp()
#not accessible print(a.__name)  for access indirectly we can use object._classname__name by anme mangling
print(a._emp__name)
