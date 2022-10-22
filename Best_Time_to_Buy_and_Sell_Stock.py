n=int(input())
l=list(map(int,input().split()))
s=0
o=[]
h=[]
for i in range(len(l)):
    o=[]
    for j in range(i+1,len(l)):
        if(l[i]<l[j]):
            o.append(l[j])
    if len(o)!=0:
        h.append(max(o)-l[i])
if len(h)!=0:
    print(max(h))
else:
    print("0")