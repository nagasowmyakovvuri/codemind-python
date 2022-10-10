n=int(input())
while n!=0:
    k=int(input())
    c=""
    while k!=0:
        f=k%2
        c+=str(f)
        k=k//2
    c=c[::-1]
    print(c)
    n-=1