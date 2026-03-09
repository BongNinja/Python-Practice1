# We are printing Pyramid Pattern
k =  int(input("Enter the no of rows to be printed \n"))
for i in range(k):
    j=k
    while j>=i:
        print(" ",end = "")
        j-=1
    l = 0
    while l<=i:
        print("* ",end = "")
        l+=1
    print("\n")