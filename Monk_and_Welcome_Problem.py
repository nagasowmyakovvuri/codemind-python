n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
k=0
l=[]
for i in range(0,n):
    k=a[i]+b[i]
    l.append(k)
print(*l)
