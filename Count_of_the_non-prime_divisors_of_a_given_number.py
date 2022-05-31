def is_prime(a):
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return 1
    if a==1:
        return 1
    return 0
n=int(input())
c=0
for i in range(1,n+1):
    if(n%i==0):
        if is_prime(i):
            c=c+1
print(c)