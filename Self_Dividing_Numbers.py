def is_prime(a):
    k=len(str(a))
    c=0
    s=a
    r=0
    while(a!=0):
        r=a%10
        if r!=0:
            if(s%r==0):
                c=c+1
        a=a//10
    if k==c:
        return 1
    return 0
n=int(input())
m=int(input())
i=n
while i<=m:
    g=i
    if is_prime(g):
        print(i,end=' ')
    i=i+1
    