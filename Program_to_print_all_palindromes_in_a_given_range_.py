a=int(input())
b=int(input())
for i in range(a,b+1):
    s=0
    k=i
    while i!=0:
        r=i%10
        s=s*10+r
        i=i//10
    if s==k:
        print(s,end=' ')