try:
    x = 10 
    y = 0
    print(x/y)
except ArithmeticError as e:
    print("The error is : ",e)
except:
    print("Hey ! It return some errors in try block")