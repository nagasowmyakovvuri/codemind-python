a=int(input())
b=list(map(int,input().split()))
k=0
l=[]
for i in b:
    if i!=0:
        l.append(i)
    else:
        k+=1

while(k!=0):
    l.append(0)
    k-=1
print(*l)
