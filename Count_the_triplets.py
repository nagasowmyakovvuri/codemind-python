n=int(input())
while n!=0:
    a=int(input())
    k=list(map(int,input().split()))
    l=0
    for i in k:
        for j in k:
            for s in k:
                if i+j==s and i!=j:
                    l+=1
    if l==0:
        print("-1")
    else:
        print(l//2)
    n-=1