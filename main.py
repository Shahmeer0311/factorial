def factorial (x):
    '''This is  a reccursive function to find the factorial of an integer'''
    if x == 0 or x == 1:
        return 1
    else:
        #calling function inside a function
        return x * factorial (x-1) 
a = int(input("Enter Number"))
print(factorial.__doc__) 
print("This is the required factorial",  a , "-",factorial (a))