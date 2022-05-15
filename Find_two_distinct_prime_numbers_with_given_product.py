def is_prime(a):
    for i in range(2,a):
        if(a%i==0):
            return 0
    return 1
n=int(input())
c=0
flag=0
for i in range(1,n):
    flag=0
    for j in range(1,n):
        if(i*j==n):
            if is_prime(i) and is_prime(j):
                print(i,j)
                c=c+1
                flag=1
                break
    if flag==1:
        break
else:
    print("-1")