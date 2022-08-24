def s_factor(f):
    d=0
    for i in range(1,f+1):
        if f%i==0:
            d+=i
    return d      
n=list(map(int,input().split(',')))
g=[]
for i in n:
    k=s_factor(i)
    if k in n:
        g.append(i)
g.sort()
if len(g)==0:
    print('-1')
else:
    print(*g)