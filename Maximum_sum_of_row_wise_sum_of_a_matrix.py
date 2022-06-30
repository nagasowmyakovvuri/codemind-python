n,m=map(int,input().split())
a=[list(map(int,input().strip().split())) for i in range(n)]
l=[]
for i in range(n):
    p=0
    for j in range(m):
        p+=a[i][j]
    l.append(p)
print(max(l))