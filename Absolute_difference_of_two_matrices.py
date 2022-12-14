
n=int(input())
a=[list(map(int,input().strip().split()))for i in range(n)]
p=0
b=[list(map(int,input().strip().split()))for i in range(n)]
for i in range(0,n):
    k=[]
    for j in range(0,n):
        g=abs(a[i][j]-b[i][j])
        if j!=n-1:
            print(g,end=" ")
        else:
            print(g)