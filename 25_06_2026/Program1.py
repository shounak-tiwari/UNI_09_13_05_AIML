# Class 
class Prog:
    Name = "Null"
    def Intro():
        print("Hello Dear students wellcome universal informatics ")


Prog.Name="Akash"
print(Prog.Name)
Prog.Intro()

# Object of class
Obj_1 = Prog
Obj_1.Intro()
Obj_1.Name = "Humid"

print(Obj_1.Name) #Akash
Obj_2 = Prog 
print("The value of class att. from Object sec : ",Obj_2.Name)