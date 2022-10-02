n=int(input())
k=map(int,input().split())
s=0
for i in k:
    if i>=n:
        s+=1
if s==0:
    print("YES")
else:
    print("NO")