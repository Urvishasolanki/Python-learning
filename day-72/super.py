#the super() keyword in python is used to refer to the parent class
class parentClass:
    def parent_method(self):
        print("this is the parent method")

class childClass(parentClass):
    def parent_method(self):
        print("this is the parent method of child")

    def child_method(self):
        print("this is the child method")
        super().parent_method()

child_object = childClass()
child_object.child_method()
child_object.parent_method()


