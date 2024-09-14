class Circle:
    def __init__(self,redius):
        self.redius = redius

    def __str__(self):
        return 'redius of the circle is: {}'.format(self.redius)
    def __add__(self,other_circle):
        return Circle(self.redius+other_circle.redius)
    
c1=Circle(2)
c2=Circle(6)
c3=c1+c2
print(c3)
