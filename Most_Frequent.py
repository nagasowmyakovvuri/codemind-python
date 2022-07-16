n=int(input())
l=list(map(int,input().split()))
k=[]
d=set(l)
d=list(d)
for i in d:
    k.append(l.count(i))
o=max(k)
s=[]
for i in d:
    if l.count(i)==o:
        s.append(i)
print(min(s))