n,m=map(int,input().split())
a=[list(map(int,input().strip().split()))for i in range(n)]
p=0
for i in range(0,n):
    k=[]
    for j in range(0,m):
        k.append(a[i][j])
    #print(k)
    f=sorted(k)
    h=f[::-1]
    if f==k or h==k:
        p+=1

print(p)