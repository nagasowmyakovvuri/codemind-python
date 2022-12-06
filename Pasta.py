n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in b:
    if b.count(i)>a.count(i):
        print('No')
        break
else:
    print('Yes')