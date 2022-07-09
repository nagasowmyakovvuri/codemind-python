n=int(input())
l=list(map(int,input().split()))
d=[]
p=0
for i in l:
    if l.count(i)==i:
        d.append(i)
        p+=1
if p!=0:
     print(min(d),max(d))
else:
    print('-1')