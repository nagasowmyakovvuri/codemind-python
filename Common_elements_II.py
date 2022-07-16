n,m=map(int,input().split())
l=list(map(int,input().split()))
h=list(map(int,input().split()))
p=[]
for i in l:
    if i not in h:
        if i not in p:
            p.append(i)
for i in h:
    if i not in l:
        if i not in  p:
            p.append(i)
print(*p)