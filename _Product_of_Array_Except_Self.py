n=int(input())
l=list(map(int,input().split()))
k=1
h=[]
for i in l:
    k=1
    for j in l:
        if i!=j:
            k=k*j
    h.append(k)
print(*h)
    