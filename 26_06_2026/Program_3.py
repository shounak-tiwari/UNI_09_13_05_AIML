#  Parameterized Constructor 
class IntroCls:
    def __init__(self,N,A):
        self.Name =N
        self.Age = A 

    def introOut(self):
        print("The name of employee : ",self.Name)
        print("The age of employee : ",self.Age)


Obj = IntroCls('Universal',32)
Obj.introOut()

'''
How many types of parameters in python ? 
a. 2 
b. 3
c. 1
d. 4 

positional 
default 
*arg
**kwargs
'''