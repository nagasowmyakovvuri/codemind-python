n=int(input())
for _ in range(0,n):
    p=int(input())
    l=list(map(int,input().split()))
    o=0
    d=0
    s=0
   # print(l)
    for i in range(0,p):
        o=0
        d=0
        for j in range(0,i):
            o+=l[j]
        for k in range(i+1,p):
            d+=l[k]
       # print(o,d)
        if o==d:
            s+=1
    if s>0:
        print("YES")
    else:
        print("NO")