n=int(input())
l=list(map(int,input().split()))
k=[]
f=[]
for i in l:
    if i%2==0:
        k.append(i)
    else:
        f.append(i)
for i in f:
    k.append(i)
print(*k)