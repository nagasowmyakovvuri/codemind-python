n=int(input())
t=n
while t!=0:
    for i in range(1,n-1):
        print(i,end='')
    for i in range(1,n-2):
        print(i,end='')
    print()
    t=t-1