# decorators :  decorate the functionallity of function without changing in code , that means decorators is an methods or process where we change the functionallity of function without changing in main code 
# how to pass  function as functions args 
def deco(x):
    def innerfunction():
        print("Hello Akash !")
        x()
    return innerfunction

@deco
def greet():
    print("Good Morning hope your day is like ______ ")

@deco
def morning():
    print("Hey Good Morning Devendra !!! ")

# greet()
morning()