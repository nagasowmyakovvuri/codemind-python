n=input()
n=n.lower()
k=''
for i in n:
    if i not in k and i!=' ':
        k+=i
k=list(k)
k.sort()
for i in k:
    print(i,end='')