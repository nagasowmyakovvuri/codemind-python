n=int(input())
m=int(input())
a=[list(map(int,input().strip().split()))for i in range(n)]
s=0
f=0
for i in range(0,n):
    for j in range(0,m):
        f+=a[i][j]
print(f)
