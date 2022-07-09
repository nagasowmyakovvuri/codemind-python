n=int(input())
l=list(map(int,input().split()))
s=0
d=0
g=max(l)
if g<0:
   d=1
x=str(g)
a=len(x)
if d==1:
    a=a-1
for i in l:
    p=0
    if i<0:
        p=1
    k=str(i)
    j=len(k)
    if p==1:
        j=j-1
    if j==a:
        s+=1
print(s)
    