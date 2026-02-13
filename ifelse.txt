# Code for If Else If Elif 
# we will be using If Else with even and odd number case
print("enter the number which you want to know whether it is even or odd \n")
K = int(input("No. :\t "))
if K==0:
   print("0 is neither even nor odd")
elif K%2 != 0:
    print(" The number is odd ")
else:
    print("The number is even ")