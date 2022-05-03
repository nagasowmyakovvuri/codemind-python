n=int(input())
while(n>0):
    l,r=map(int,input().split())
    c=0
    for i in range(l,r+1):
        k=i%10
        if k==2 or k==3 or k==9:
            c=c+1
    print(c)
    n=n-1
    