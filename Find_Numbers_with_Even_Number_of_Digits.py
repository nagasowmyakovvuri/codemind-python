n=int(input())
a=list(map(int,input().split()))
k=0
for i in range(0,n):
    c=0
    while(a[i]!=0):
        c=c+1
        a[i]=a[i]//10
    if c%2==0:
        k+=1
print(k)