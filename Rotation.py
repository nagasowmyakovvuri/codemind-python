n=int(input())
for _ in range(0,n):
    k,m=map(int,input().split())
    g=list(map(int,input().split()))
    j=[]
    for i in range(abs(k-m),k):
         j.append(g[i])
    for i in range(0,abs(k-m)):
        j.append(g[i])
    print(*j)

    