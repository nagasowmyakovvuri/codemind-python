def is_prime(a):
    for i in range(2,a):
        if a%i==0:
            return 0
    if a==1:
        return 0
    return 1
n=int(input())
m=int(input())
k=n+m
i=1
while(1):
    l=i+k
    if(is_prime(l)==1):
        print(i)
        break
    i=i+1
