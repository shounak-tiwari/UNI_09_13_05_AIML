# nested functions inner return from outer functions 
def outerFun():
    def innerFun():
        print("Inner function executed successfully")
    return innerFun()

# calling of outer function     
outerFun()