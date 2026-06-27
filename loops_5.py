#enter a number and check number is arm strong or not...  
#enter a number and check digit count in a number....
 
# # Algo - 1
# import math
# number = 12345
# x = 12345
# print(int(math.log10(x)))

# Algo - 2
number = 153
original = number
temp = number
counter = 0 
while number%10 !=0:
    counter+=1
    number//=10
add = 0
while original !=0:
    add = add + ((original%10)**counter)
    original//=10
if temp == add:
    print("armstrong")
else:
    print("not armstrong")