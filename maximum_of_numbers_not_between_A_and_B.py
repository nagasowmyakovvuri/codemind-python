n=int(input())
a=list(map(int,input().split()))
m,n=map(int,input().split())
k=[]
l=0
for i in a:
    if i<m or i>n:
        k.append(i)
        l=l+1
if l>0:
    print(max(k))
else:
    print("-1")