# distructor : is special methods named __del__ , it is automatically called when an object is about to be destroyed primily used to clean up non memory resouces like closing open files or network
class demo:
    def __init__(self):
        print("Hey Guys! Good Morning ")
    def __del__(self):
        print("Hey im from demo class ")

class Prog:
    def __init__(self):
        self.name = input("Enter the name of student : ")
    
    def introOut(self):
        print("The name of Student : ",self.name)
    
    def __del__(self):
        print("Memory getting distroy and clean your resources ")
    
Obj = Prog()
Obj.introOut()
Obj2= Prog()
Obj2.introOut()
objDemo1 = demo()
obj3 = Prog()