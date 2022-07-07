def is_prime(a):
    for i in range(2,a):
        if a%i==0:
            return 0
    return 1
n=int(input())
k=n
s=0
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
if is_prime(k)==1 and is_prime(s)==1:
    print("circular prime")
elif is_prime(k)==1 and is_prime(s)!=1:
    print("prime but not a circular prime")
else:
    print("not prime")
