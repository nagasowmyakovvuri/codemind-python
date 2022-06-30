n,m=map(int,input().split())
a=[list(map(int,input().strip().split())) for i in range(n)]

o=[]
p=0
for i in range(m):
    p=0
    for j in range(n):
        p+=a[j][i]
    o.append(p)
print(*o)