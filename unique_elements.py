n=int(input())
a=list(map(int,input().split()))
l=set(a)
k=list(l)
##print(a)
d=[]
for i in a:
    c=0
    for j in a:
        if i==j and i not in d:
            c=c+1
            d.append(i)
print(*d)