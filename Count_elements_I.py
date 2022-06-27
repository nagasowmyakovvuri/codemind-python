n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
k=0
a=set(a)
b=set(b)
for i in a:
    if i in b:
        k+=1
print(k)