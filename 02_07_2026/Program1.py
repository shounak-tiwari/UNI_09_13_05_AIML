# Create a class 
# what is imp of pass keywords : you function declare but the defination of functions or function statements , or logic write after sometime or later on ... 

class Base:
    def Intro(self):
        print("Hello Universal informatics indore!!! ")


class Derived(Base):
    def Intro(self):
        print("Hello this is akash tiwari")


obj = Derived()
obj.Intro()