n=int(input())
while n!=0:
    k=int(input())
    l=bin(k)
    print(l.count('1'))
    n-=1