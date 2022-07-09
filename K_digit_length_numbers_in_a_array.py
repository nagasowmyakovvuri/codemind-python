n,m=map(int,input().split())
l=list(map(int,input().split()))
s=0
for i in l:
    p=0
    if i<0:
        p=1
    k=str(i)
    j=len(k)
    if p==1:
        j=j-1
    if j==m:
        s+=1
print(s)
    