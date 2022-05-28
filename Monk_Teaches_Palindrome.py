n=int(input())
while n!=0:
    a=input()
    if a[: :-1]==a:
        print("YES",end=' ')
        if(len(a)%2==0):
            print("EVEN")
        else:
            print("ODD")
    
    else:
        print("NO")
    n-=1