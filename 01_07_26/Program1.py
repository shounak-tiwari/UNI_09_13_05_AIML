'''
Inheritance : Multilevel Inheritance 

base class 
    |
intermidate class 
    |
child class 
'''

class Base:
    def __init__(self,x):
        self.Name = x
    
class Intermidate(Base):
    def __init__(self, x,y):
        super().__init__(x)
        self.Age = y
    
class ChildClass(Intermidate):
    def __init__(self, x, y,z):
        super().__init__(x, y)
        self.contact = z
    
    def output(self):
        print("The name of employee : ",self.Name)
        print("The age of employee : ",self.Age)
        print("The Contact of employee  : ",self.contact)
    

obj  = ChildClass("Name","26","Universal front office team")
obj.output()