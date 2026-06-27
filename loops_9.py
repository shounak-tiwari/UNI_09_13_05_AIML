# write a program for print 1 to n prime numbers ? 
n = 10 
j= 1
while j<= n:
    factor = 0 
    i = 1
    while i<=j:
        if j%i ==0:
            factor += 1
        i += 1
    if factor == 2 :
        print(j,"is prime")
    else:
        print(j," is not prime")
    j+=1