def check(n):
    if n=='000':
        return '0'
    elif n=='001':
        return '1'
    elif n=='010':
        return '2'
    elif n=='011':
        return '3'
    elif n=='100':
        return '4'
    elif n=='101':
        return '5'
    elif n=='110':
        return '6'
    elif n=='111':
        return '7'
n=int(input())
for _ in range(0,n):
    k=input()
    if len(k)%3!=0:
        f=3-len(k)%3
        a=""
        for i in range(0,f):
            a+='0'
        k=a+k
    s=""
    for i in range(0,len(k),3):
        a=""
        a+=k[i]
        a+=k[i+1]
        a+=k[i+2]
        s+=check(a)
    print(s)
        