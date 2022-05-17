def is_dividing(a):
    r=0
    c=0
    l=a
    k=len(str(a))
    while a!=0:
        r=a%10
        if r!=0:
            if l%r==0:
                c=c+1
        a=a//10
    if k==c:
        return 1
    return 0
n=int(input())
m=int(input())
for i in range(n,m+1):
    f=i
    if is_dividing(i)==1:
        print(f,end=' ')