n=int(input())
l=list(map(int,input().split()))
f=0
for i in range(2,len(l)):
    if l[i]==l[i-1]+l[i-2]:
        f=1
    else:
        f=0
        break
if f==0:
    print("no")
else:
    print("yes")