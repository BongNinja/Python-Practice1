# This program deals with the  break statement
k = int(input("Provide the no of iterations "))
for i in range(k):
    if k <=5:
        print("LED%d will glow \n"%(i+1))
    elif k>5:
        break
if k>5:
    print("Only 5 LEDs are present in the circuit \n")
