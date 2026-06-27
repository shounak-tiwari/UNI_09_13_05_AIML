# high order : sorted , map ,filter , reduce 

# reduce : aggr.. which is use for summrise the data 

# print sum of  1 to n even number 
# import module 
from functools import reduce


# create lambda for expression and conditions and args 

lst = list(range(1,int(input("Enter the number : "))))
print(lst)

red = lambda x:x%2==0

print(reduce(red,lst))