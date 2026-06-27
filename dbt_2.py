# remove duplicates from lists
# creating list 
lst = [1,2,3,4,5,6,3,6,7]
# creating empty list 
result = []
for x in lst:
    if x not in result:
        result.append(x)
print(result)
