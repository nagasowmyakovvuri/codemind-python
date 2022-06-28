n=int(input())
while n!=0:
    a=int(input())
    d=[]
    k=[]
    j=[]
    l=list(map(int,input().split()))
    for i in range(0,a//2):
        d.append(l[i])
    ##print(d)
    for i in range(a//2,a):
        k.append(l[i])
   
    k.reverse()
    ##print(k)
    for i in range(0,a//2):
        j.append(k[i])
        j.append(d[i])
    
    if len(j)!=len(l):
        for i in l:
            if i not in j:
               j.append(i)
    
    print(*j)
    
    n-=1