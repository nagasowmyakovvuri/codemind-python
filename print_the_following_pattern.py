n=int(input())
for i in range(n-1,-1,-1):
    for j in range(0,i+1):
        print(chr(65+i),end=' ')
    print()
    