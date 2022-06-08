a=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(0,a,2):
    k=b[i+1]
    while(k!=0):
        c.append(b[i])
        k-=1
print(*c)