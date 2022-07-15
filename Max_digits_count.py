n=int(input())
l=list(map(int,input().split()))
k=max(l)
j=str(k)
s=len(j)
p=0
for i in l:
    if len(str(i))==s:
        p+=1
print(p)