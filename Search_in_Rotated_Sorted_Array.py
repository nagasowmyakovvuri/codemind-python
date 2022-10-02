n=int(input())
k=list(map(int,input().split()))
l=int(input())
for i in range(0,n):
    if k[i]==l:
        print(i)
        break
else:
    print("-1")