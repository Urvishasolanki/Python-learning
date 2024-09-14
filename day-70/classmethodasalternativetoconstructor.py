class Employee():
    def __init__(self,name,no):
        self.name=name
        self.no=no
    
    @classmethod
    def form_str(cls,str):
        return cls(str.split(",")[0],str.split(",")[1])
    
e1=Employee("urvisha",1)
print(e1.name)
print(e1.no)
string="piya-2"
e2= Employee.form_str(string)
print(e2.name)
print(e2.no)


