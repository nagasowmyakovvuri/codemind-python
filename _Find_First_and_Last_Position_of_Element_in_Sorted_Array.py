n=int(input())
l=list(map(int,input().split()))
a=int(input())
l.sort()
p=0
for i in range(len(l)):
    if l[i]==a:
        print(i,end=" ")
        k=i
        p=p+1
if p==1:
    print(k)
if p==0:
    print("-1","-1")
    