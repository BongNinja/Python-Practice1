# We are splitting the string and reversing the words 
s = input("Enter the input string \n")
k = s.split()
print(k)
result = []
i = len(k)-1
print(i)
while i>=0:
    result.append(k[i])
    i-=1
print(result)
t = ' '.join(result)
print(t)