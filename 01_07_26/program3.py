# write a program for calculating area of triangle... using abstractions 

# abstract : where we have declaration of function but dosen't provide any type of definations 

# abstract class is an type class whose object is not possible to create 

from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def area(self,x,y):
        return x*y

class Child(Base):
    def area(self,x,y):
        return super().area(x,y)

obj = Child()
print("The area is : ",obj.area(10,20))