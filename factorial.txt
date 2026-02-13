# factorial code
a = 1
print("enter the number whose factorial you want to know: \n")
n = int(input("Enter here : "))
k=n
for i in range(k):
    a = a*n
    n-=1
print(" the factorial of the given number is \t %d" %a)