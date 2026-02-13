# A code to generate average of three numbers 
L = []
k=int(input("start :"))
print("Start giving input values for the average operation: \n ")
if k>0:
    for i in range(k):
        L.append(int(input()))
else:
    print("no value")
print(L)
print(type(L))
print("\n Now the average of the numbers is shown below \n")
result = 0

for j in range(k):
    result = result + L[i] + L[k-1-i]
print(result/2)
print(result/(2*k))