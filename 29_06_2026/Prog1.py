'''
Access Specifiers in python : 
1. public : attributes are call from anywhere , not use of single and double underscore 
2. private : attributes is not call from outside of the class use __ double underscore before 
3. protected  : attributes are call only from child classes for defining the protected attributes we have to use single underscore 
'''
# encapsulation is one of piller of object oriented programming ,which is wrape the data inside a single unit... 

class Main:
    def setter(self,x):
        self.__name = x
    def getter(self):
        return self.__name
    
obj = Main()
obj.setter("Hey! Monday")
print(obj.getter())