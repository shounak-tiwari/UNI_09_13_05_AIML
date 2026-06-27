class Prog:
    def Intro(x):
        x.Name = input("Enter the name  : ")
        print(f"Good Morning {x.Name} Hope your day is as your smile :) ")
        
    def SavetoDb(x):
        print(x.Name)


# Create the object of Prog
obj1 =  Prog()
obj1.Intro()
obj1.SavetoDb()