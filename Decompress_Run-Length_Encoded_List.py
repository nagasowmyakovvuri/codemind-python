n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(0,len(l)-1,2):
    for j in range(l[i]):
        k.append(l[i+1])
print(*k)