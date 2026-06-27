class Students:
    # class methods 
    def Intro(instance):
        instance.name =input("Enter the name of student : ")
        print("Hello ! Good Morning Hope your day is like as smile ")
    
    def output(instance):
        print(instance.name)
    
Obj = Students()
Obj.Intro()
Obj.output()