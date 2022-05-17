def fibnaco(k):
    a=0
    b=1
    for i in range(3,k):
        c=a+b
        if c==k:
            return ("True")
        a,b=b,c
    return ("False")
n=int(input())
print(fibnaco(n))