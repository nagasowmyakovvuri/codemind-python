n=int(input())
l=list(map(int,input().split()))
for i in l:
    p=0
    j=0
    if i<0:
        p=1
    k=str(i)
    j=len(k)
    if p==1:
        j=j-1
    print(j,end=' ')
    