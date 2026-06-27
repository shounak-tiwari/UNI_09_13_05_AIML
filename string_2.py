string = "universal informatics"

# print(string)

# upper case : upper 
# lower case : lower
# capitalize : first latter convert into upper case and rest is lower 
# title : first latter of all words convert into upper case 
# print(string.capitalize())
# print(string.title())

# join method of string class 
# s1 = "_"
# s2 = "Universal"
# print(s1.join(s2))

#casefold : those latters present in upper case it convert into lower case

# s1 = "    UniVersal     "
# print(s1.casefold())
# print(s1.strip())


# s1 = "universal informatics"
# print(s1[::-1])

# s1 = "univerSAL"
# print(s1.swapcase())

# find(sub) :  return first index or -1 
s1 = "the student of universal informatics indore is future of indore"
print(s1.find("indore"))

# rfind(sub) : return the last index 
print(s1.rfind("indore"))

# index(sub): like find() raise error if not found
print(s1.index("indore"))

# index(sub): like find() raise error if not found
print(s1.rindex("indore"))

# count()
#  startswith()
# endswith()

s1 = "raj"

s1 = s1.replace("raj","patel")

print(s1)
