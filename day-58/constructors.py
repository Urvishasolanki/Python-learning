class person:
    name="harry"
    occ="devloper"
    
    def info(self):
        print(f"{self.name} is a {self.occ}")
a=person()
print(a.name)
a.name="urvisha"
a.occ="web devloper"
a.info()
