# what is class ? 
class Demo:
    # class based attributes 
    Name = ""
    Contact = ""


# object 1 is object of demo 
obj1 = Demo 
obj2 = Demo

obj1.Name = "UniTeleCom"
obj1.Contact="UniTeleCom branch in bhawarkua"

obj2.Name = "Universal-2nd branch"
obj2.Contact="Universal 2nd branch in bhawarkua"

print("The name of Object 1 : ",obj1.Name)
print("The contact of Object 1 : ",obj1.Contact)


print("The name of Object 1 : ",obj2.Name)
print("The contact of Object 1 : ",obj2.Contact)

print(Demo.Name)
print(Demo.Contact)

# class based attributes  : this attributes is change their values from any updated object 