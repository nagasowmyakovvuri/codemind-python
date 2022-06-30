n,m=map(int,input().split())
a=[list(map(int,input().strip().split()))for i in range(n)]
s=0
p=0
for i in range(0,m):
    f=[]
    for j in range(0,n):
        f.append(a[j][i])
    print(max(f))
