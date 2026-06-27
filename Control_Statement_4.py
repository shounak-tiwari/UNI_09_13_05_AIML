#calculate electricity bill according to consuptions 
# enter units and where as if the 
# a. unit is <=100  pay 0.5 rs per unit 
# b. unit >100 and unit <=200  pay 1.0 rs per unit  
# c. unit >200 and unit <=300  pay 1.5 rs per unit  
# d. unit >301 and unit <=400  pay 2.0 rs per unit  
amount =0 
unit = int(input("enter the units :  "))
if unit<=100:
    amount = 0.5*unit
elif 100<unit<=200:
    amount = 1.0*unit
    
amount = amount + ((amount*50)/100)
print("Total Payable Amount : ",amount)