# We will create a diamond 
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
for m in range(k):
    j=0
    while j<=m:
        print(" ",end = "")
        j+=1
    l = k-1
    while l>=m:
        print(" *",end = "")
        l-=1
    print("\n")