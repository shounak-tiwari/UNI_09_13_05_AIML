
number = 1
while number<=1000:    
    original = number
    temp = number
    counter = 0 
    while number!=0:
        counter+=1
        number//=10
    add = 0
    while original !=0:
        add = add + ((original%10)**counter)
        original//=10
    if temp == add:
        print(number)
    number+=1