n=int(input())
l=list(map(int,input().split()))
p=0
s=[]
for i in range(len(l)-1,0,-1):
    s=[]
    for j in range(0,i):
        s.append(l[j])
    #print("j")
    k=max(s)
    #print(s)
    if l[i]<k:
        l[l.index(k)],l[i]=l[i],l[l.index(k)]
        p+=1
print(p)
        