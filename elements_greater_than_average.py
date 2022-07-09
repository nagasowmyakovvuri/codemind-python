n=int(input())
l=list(map(int,input().split()))
k=sum(l)
s=k//len(l)
p=0
for i in l:
    if i>=s:
        p+=1
print(p)