n=int(input())
l=list(map(int,input().split()))
m=int(input())
p=[]
k=[]
f=[]
for i in range(0,n//2):
    p.append(l[i])
for i in range(n//2,n):
    k.append(l[i])
for i in range(0,n//2):
    f.append(p[i])
    f.append(k[i])
print(*f)