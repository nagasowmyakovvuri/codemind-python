def lcm(n,k):
    f=[]
    
    f.append(n)
    f.append(k)
    v=max(f)
    while (1):
        if(v%min(f)==0) and v%max(f)==0:
            return v
            break
        else:
             v+=1
n=int(input())
l=list(map(int,input().split()))
i=0
s=l[i]
#print(l)
for i in range(len(l)-1):
    s=lcm(s,l[i+1])
    
print(s)