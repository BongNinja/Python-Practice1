#This code will handle Input Output functions 
#This code is an Ice Cream  Ordering  Program
print("What Ice cream do you want select from the options below :-")
L = [35," Vanilla",40, " Chocolate",50, " Butter Scotch",55, " Strawberry",45, " Kaju Katli",30, " Mango",40, " Rasmalai" ]
k = len(L)
for  i in  range(1,k,2):
    print(L[i])
    print("\n")
C = input("Your Input")

for j in range(k):
    if (C==L[j]):
        print("Please pay your price ",L[j-1])
        print("\n")
print("Would You Pay (1) online \n or by \n (2) cash\n")
l = input()
if(l==1):
    print("Scan the QR and pay your price or use internet banking/debit cards\n")
if(l==2):
    print("Pay the cash at the counter")
print("input 'done' if it is so ")
input()
print(" Thank You! \n rate us and Please Visit us again")
