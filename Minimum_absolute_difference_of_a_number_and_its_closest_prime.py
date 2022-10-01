def is_prime(a):
    for i in range(2,a):
        if a%i==0:
            return 0
    else:
        return 1
n=int(input())
k=[]
for i in range(1,n):
    i=i+n
    if is_prime(i)==1:
        k.append(i-n)
        break

for i in range(1,n):
    
    if is_prime(n-i)==1:
        ##print(n-i)
        k.append(n-(n-i))
        break
##print(k)
if is_prime(n)==1:
    print("0")
else:
    print(min(k))