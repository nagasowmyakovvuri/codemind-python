n=int(input())
while n!=0:
    m=int(input())
    l=list(map(int,input().split()))
    k=list(map(int,input().split()))
    p=[]
    for i in l:
        if i not in p:
            p.append(i)
    for i in k:
        if i not in p:
            p.append(i)
    if len(p)>=m:
        print("YES")
    else:
        print("NO")
    n-=1