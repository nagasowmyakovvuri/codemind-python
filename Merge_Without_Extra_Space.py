a=int(input())
while a!=0:
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    f=list(map(int,input().split()))
    i=0
    g=[]
    for i in s:
        g.append(i)
    for i in f:
        g.append(i)
    g.sort()
    print(*g)
    a=a-1