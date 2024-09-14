class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def showDetails(self):
        print(f"the name of employee: {self.id} is {self.name}")


class programmer(employee):
    def showLanguage(self):
        print("the default language is python")

e=employee("urvisha",50)
e.showDetails()
p=programmer("urvi",21)
p.showDetails()
p.showLanguage()