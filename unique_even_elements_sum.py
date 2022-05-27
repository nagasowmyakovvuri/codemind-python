n=int(input())
a=list(map(int,input().split()))
c=set(a)
d=list(c)
count=0
for i in d:
    if i%2==0:
        count=count+i
print(count)
