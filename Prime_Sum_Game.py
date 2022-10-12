def is_prime(n):
    if n==1:
        return 0
    for i in range(2,(n//2)+1):
        if(n%i==0):
            return 0
    else:
        return 1
n,m,a,b=map(int,input().split())

for i in range(n,m+1):
    f=0
    for j in range(a,b+1):
        if(is_prime(i+j)==1):
            f=1
            break
    if(f==0):
        print("Takahashi")
        break
else:
    print("Aoki")