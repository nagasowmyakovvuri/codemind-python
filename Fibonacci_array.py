n=int(input())
a=list(map(int,input().split()))
p=0
for i in range(2,n):
    if a[i]==a[i-1]+a[i-2]:
        p=1
    else:
        p=0
        break
if p==0:
    print("no")
else:
    print("yes")