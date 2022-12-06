n=int(input())
while n!=0:
    k=input()
    p=int(k,16)
    l=bin(p)
    l=l.replace('0b','')
    o=len(l)
    if o%4!=0:
        f=4-len(l)%4
        A=""
        for i in range(0,f):
            A+='0'
        l=A+l
    print(l)
    n-=1