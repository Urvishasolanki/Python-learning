class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p=person("john",30)
print(p.__dict__)
#give attribute as dictionary write within self than it is come with __dict__
print(help(person))#help method give extra information about argument
print(help(str))