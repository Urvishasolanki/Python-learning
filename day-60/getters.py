class myclass:
    def __init__(self,value):
        self.value=value
    def show(self):
        print(f"value is {self.value}")
    def values(self):
        return self.value
    
obj=myclass(10)
print(obj.value) 
obj.show()