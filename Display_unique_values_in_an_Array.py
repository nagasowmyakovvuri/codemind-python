n=int(input())
a=list(map(int,input().split()))
k=0
b=set(a)
f=[]
p=0
for i in b:
    if a.count(i)==1:
        f.append(i)
        p+=1
if p>0: 
    print(*f)
else:
    print("-1")
