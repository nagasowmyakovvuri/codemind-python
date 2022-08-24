n=int(input())
l=list(map(int,input().split()))
d=set(l)
for i in d:
    if l.count(i)>n//2:
        print(i)
