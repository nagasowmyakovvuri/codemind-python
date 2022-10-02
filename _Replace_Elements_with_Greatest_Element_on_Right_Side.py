n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(0,n-1):
    p=[]
    i=i+1
    for j in range(i,n):
        p.append(l[j])
    ##print(max(p))
    k.append(max(p))
k.append(-1)
print(*k)