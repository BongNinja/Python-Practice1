#Introduction to functions in Python  
# We will be creating some functions 

#Average of two Numbers
#defining the function
def Avg(a,b):
    print("the average of the two numbers passed is \n",(a+b)/2)

#calling the function 
Avg(1,2)

#Product of Two numbers
#defining the function 
def Prod(a,b):
    return a*b
#calling the function with return type
ans = Prod(3,6)
print(f"The Product of the two numbers is  {ans}")