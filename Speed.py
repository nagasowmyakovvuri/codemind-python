n=int(input())
while n!=0:
    k=int(input())
    d=list(map(int,input().split()))
    g=0
    for i in range(0,k-1,1):
        if d[i]>=d[i+1]:
            g+=1
    print(g+1)
    n-=1