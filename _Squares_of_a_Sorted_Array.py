n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    a[i]=a[i]*a[i]
##print(a)
a.sort()
print(*a)