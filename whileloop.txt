# In this code we will be working with the while loop 
# Display Numbers from 1 to 20 
print(" Do you want us to display numbers for a given range: \n")
a = input(" Yes or No : \t")
if a == "Yes":
    print(" tell us the range starting from 1 upto which the numbers are to be displayed : \n")
    k = int(input("range upto \t"))
    i=1
    while i <= k:
        print(" %d \t" %i)
        i+=1
else :
    print(" No input received")