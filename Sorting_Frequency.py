n=int(input())
l=list(map(int,input().split()))
k=[]
h=[]
for i in l:
    if i not in k:
        k.append(i)
for i in k:
    if l.count(i) not in h:
        h.append(l.count(i))
h.sort()
h.reverse()
#print(h)
p=[]
f=[]
for i in h:
    p=[]
    for j in k:
        if l.count(j)==i:
            p.append(j)
    p.sort()
    for v in p:
        f.append(v)
print(*f)