n=int(input())
a=list(map(int,input().split()))
for i in range(n-1,int(n//2)-1,-1):
    print(a[i],end=' ')
for i in range(n//2):
    print(a[i],end=' ')