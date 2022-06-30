n=int(input())
m=list(map(int,input().split()))
l=[]
k=set(m)
p=0
for i in k:
    if m.count(i)==1:
        l.append(i)
        p+=1
if p>0:
    print(max(l))
else:
    print("-1")
