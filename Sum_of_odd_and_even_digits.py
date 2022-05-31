n=int(input())
a=list(map(int,input().split()))
k=0
l=0
for i in range(0,n):
    if i%2==0:
        k=k+a[i]
    else:
        l=l+a[i]
if k==l:
    print("YES")
else:
    print("NO")