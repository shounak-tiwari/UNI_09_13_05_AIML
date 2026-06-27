"""
Control Statement : statement which control the flow of execution of program based on some conditions
1. if 
2. if else 
3. if elif else 
4. nested if 
5. nested if else 
6. match-case (3.9+ version)
7. loops 
"""
# Write a program to check use is eligible for vote or not 
age = int(input("Enter the age of user : "))
if age>=18:
    print("User can vote")
else:
    print("User can not vote")