# and :  when 'and' is use between two or more operands, it return true when all return True otherwise return false 
# or : when 'or' is use between two or more operands, it return true when anyone from two or all  return True otherwise return false
# not  : change the true into false and false into true 
# enter name of candidate and check its len is > from 2 or < 8 if it is more 8 name is invalid...  
'''
enter the name 
'''
name = input("Enter the name  : ")
# len() : is use for calculation of length of container like string , list , dict , set etc.... 
print(len(name)>2 and len(name)<8)
# when both conditions return true then only it return true...... 