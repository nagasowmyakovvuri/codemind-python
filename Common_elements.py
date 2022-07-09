n,m=map(int,input().split())
l=list(map(int,input().split()))
p=list(map(int,input().split()))
##print(l)
##print(p)
p=set(p)
p=list(p)
s=[]
for i in l:
    if i in p:
        if s.count(i)==0:
            s.append(i)
print(*s)