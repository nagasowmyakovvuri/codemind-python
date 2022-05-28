def is_square(a):
    for i in range(1,a+1):
        if(i*i==a):
            return 1
            break
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    if(is_square(i)):
        s=s+i
print(s)