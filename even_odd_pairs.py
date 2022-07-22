n=int(input())
l=list(map(int,input().split()))
k=[]
m=[]
for i in l:
    if i%2==0:
        k.append(i)
    else:
        m.append(i)

o=[]
i=0
if len(k)>len(m):
    for i in range(len(m)):
        o.append(k[i])
        o.append(m[i])
    for i in range(len(m),len(k)):
        o.append(k[i])
        
    
elif len(k)<len(m):
    i=0
    for i in range(len(k)):
        o.append(k[i])
        o.append(m[i])
    for i in range(len(k),len(m)):
        o.append(m[i])
        
    
    
else:
    i=0
    for i in range(len(m)):
        o.append(k[i])
        o.append(m[i])
if len(o)%2!=0:
    o.append(0)
print(*o)
    
    
        