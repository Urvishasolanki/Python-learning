class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang = lang

riya=Employee("urvisha","40")
priya=programmer("urvi","30","English")
print(priya.id)
print(priya.name)
print(priya.lang)

