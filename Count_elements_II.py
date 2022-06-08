n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
k=set(a)
l=set(b)
p=0
for i in k:
    if i not in l:
        p+=1
for i in l:
    if i not in k:
        p+=1

print(p)