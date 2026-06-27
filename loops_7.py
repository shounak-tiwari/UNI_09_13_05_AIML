Num1 =  int(input("Enter the two number : "))
Num2 =  int(input("Enter the two number : "))
maxNumber = max(Num1,Num2)
while True:
    if maxNumber%Num1 ==0 and maxNumber %Num2 ==0:
        print("LCM : ",maxNumber)
        break
    else:
        maxNumber+=1