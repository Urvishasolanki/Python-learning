#dunder method is also known as special method and start with __ and also end with __ (megic method).
class Employee:
    def __init__(self,name):
        self.name=name
        
    def __len__(self):
        i =0 
        for c in self.name:
            i = i+1
        return i
    
    def __repr__(self):
        return f"the  name of the employee is {self.name} repr"
       
    # def __str__(self):
    #     return f"the  name of the employee is {self.name}"
    
    
    
    