n,m=map(int,input().split())
a=[list(map(int,input().strip().split())) for i in range(n)]
l=[]
p=0
h=0
for i in range(n):
    
    for j in range(m):
        if i%2==0:
            p+=a[i][j]
        else:
            h+=a[i][j]
print(p,h)
