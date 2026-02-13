#counting vowels in a word
print("enter the word : \n")
k = list(input())
print(k)
print(type(k))
count = 0
for i in range(len(k)):
    if (k[i]== "A") or (k[i]=="a") or (k[i]== "E") or (k[i]== "e") or (k[i]== "I") or (k[i]== "i") or (k[i]== "o")  or (k[i]== "O") or (k[i]== "U") or (k[i]== "u"):
        count+=1
print(count)