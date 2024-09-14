class person:
    def __init__(self,name,occ):
        print("hello i am person")
        self.name=name
        self.occ=occ
    def info(self):
        print(f"{self.name} is a {self.occ}")
a=person("urvisha","full stack devloper")
a.info()
b=person("vidhya","singer")
b.info()
# always return none