# In this program odd numbers between two given numbers will be displayed 
print("enter the minimum number: \n")
min = int(input("Min. No. : \t"))
print("enter the maximum number: \n")
max = int(input("Max No : \t"))
k1 = (min+1)//2 
k2 = max//2
i = k1
while i<k2:
    c = 2*i + 1
    print("%d" %c)
    i+=1