n,pos,v=map(int,input().split())
l=list(map(int,input().split()))
d=[]
for _ in range(0,v):
    d.append(int(input()))
k=[]
s=[]
for i in l:
    k.append(i)
for i in l:
    k.append(i)
if(pos>n):
    pos=pos%n
for i in range(n-pos,2*n-pos):
    s.append(k[i])
for i in d:
    print(s[i])