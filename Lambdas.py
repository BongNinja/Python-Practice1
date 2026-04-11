#Playing with lambdas
def Lambdas():
    k = lambda a: a**2 #square lambda function
    l = lambda b:b**3  #cube lambda function
    m = lambda c:c**1  #identity lambda function
    if s =="square":
        print(k(t))
    elif s == "cube":
        print(l(t))
    elif s == "identity":
        print(m(t))    
    else:
        print("Have a good day \n")
    return
t = int(input("Enter the number: "))
s = input("Which Lambda You wanna play with? square, cube or idenity? \n")
Lambdas()