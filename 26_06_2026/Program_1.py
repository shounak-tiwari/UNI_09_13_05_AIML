# create class 
class Prog:
    def __init__(self):
        print("hey im your constructor ")
        print("The id of self : ",id(self))



# declare object of class 
Obj = Prog()
print("id of object : ",id(Obj))


obj2 = Prog()
print("id of object : ",id(obj2))