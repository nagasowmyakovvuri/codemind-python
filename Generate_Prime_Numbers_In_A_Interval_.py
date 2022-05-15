def is_prime(a):
    for i in range(2,a):
        if a%i==0:
            return 0
    if a==1:
        return 0
    return 1
n=int(input())
m=int(input())
i=n
while(i<=m):
    if(is_prime(i)==1):
        print(i)
    i=i+1
