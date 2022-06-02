a=input()
k=0
for i in range(len(a)):
    if a[i] in "aeiouAEIOU":
        k+=1

print(k)