n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
k=set(a)
l=set(b)
p=0
for i in k:
    if i  in l:
        p+=1
print(p)