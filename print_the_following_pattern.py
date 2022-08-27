n=int(input())
for i in range(0,n-1):
    for j in range(0,n):
        if j==0 or i==j :
            print('*',end='')
        else:
            print(' ',end='')
    print()
for j in range(n):
    print('*',end='')