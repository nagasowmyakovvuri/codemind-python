def fibnaco(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibnaco(n-1)+fibnaco(n-2)
n=int(input())
for i in range(0,n):
    res=fibnaco(i)
    print(res,end=' ')