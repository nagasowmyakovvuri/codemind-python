n=int(input())
l=list(map(int,input().split()))
d=[]
for i in l:
    if d.count(i)==0:
        d.append(i)
print(*d)