# In this code we will be handling multiple inputs 
print( "provide the inputs to the system and before that mention no of inputs: " )
c = []
k = int(input())
for i in range(k):
    print(" provide input no %d \n" %i)
    c.append(int(input("here it is:\n ")))
print(c)
print(type(c))