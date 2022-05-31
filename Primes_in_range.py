def is_prime(a):
    if a<2:
        return 0
    for i in range(2,int(a**0.5)+1):
        if(a%i==0):
            return 0
    return 1
n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    if(is_prime(i)==1):
        c=c+1
print(c)