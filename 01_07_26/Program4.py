'''
Polymorphisms it is major piller of oops but python supports only runtime polymorphisms beacuse it's type of language who allocate or create memory at run time 
so python support only runtime polymorphisms basically polymorphisms have two types 
1. compile time 
    a. function overloading  : where we have more than one function with same name in a class but call or execute according to parms 
2. run time poly 
    b. function overriding 
'''
# if want work with compile time polymorphisms we can say that we can use built library which is known as MULTIPLEDISPATCH
from multipledispatch import dispatch
class Base:
    @dispatch(int,int)
    def intro(x,y):
        print("Hey my name is x  : ",x)
        print("Hey my name is y : ",y)
    @dispatch(str,int)
    def intro(x,y):
        print("The name is : ",x)
        print("The age is  : ",y)
bj = Base()
bj.intro(10,20)
bj.intro("10",20)