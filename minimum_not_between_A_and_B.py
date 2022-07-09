n=int(input())
l=list(map(int,input().split()))
k,m=map(int,input().split())
s=[]
p=0
for i in l:
    if i<k or i>m:
        s.append(i)
        p+=1
if p!=0:
    print(min(s))
else:
    print('-1')