def is_prime(a):
    if a<2:
        return 0
    for i in range(2,int(a**0.5)+1):
        if(a%i==0):
            return 0
    return 1
n=int(input())
m=list(map(int,input().split()))
c=0
k=0
for i in range(n):
    if(is_prime(m[i])==1):
        c=c+m[i]
        k+=1
print("%.2f"%(c/k))