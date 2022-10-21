n,m=map(int,input().split())
l=list(map(int,input().split()))
b=0
for i in range(0,n):
    s=0
    for j in range(i,n):
        s+=l[j]
        if(s==m):
            b+=1
print(b)