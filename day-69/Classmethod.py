class Employee:
    company = "google"
    def show(self):
       print(f"Employee name is {self.name} company is {self.company}")

    @classmethod
    def changeCompny(cls,newcompny):
        cls.company=newcompny

e1 = Employee()
e1.name = "piya"
e1.show()
e2 = Employee()
e2.name = "urvisha"
e1.changeCompny("microsoft")
e1.show()