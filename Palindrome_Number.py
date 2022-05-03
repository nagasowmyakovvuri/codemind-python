n=int(input())
while n!=0:
    a=int(input())
    k=a
    s=0
    while a!=0:
        r=a%10
        s=s*10+r
        a=a//10
    if(s==k):
        print("True")
    else:
        print("False")
    n=n-1