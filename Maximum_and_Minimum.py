n=int(input())
a=list(map(int,input().split()))
c=0
d=[]
f=[]
k=set(a)
l=list(k)
##print(l)
##print(a)
for i in l:
    c=0
    for j in a:
        if i==j:
            c=c+1
    d.append(c)
##print(d)
p=0
for i ,j in zip(l,d):
        if i==j:
            f.append(i)
            p=p+1
if len(f)>0:
    print(min(f),max(f))
else:
    print("-1")
