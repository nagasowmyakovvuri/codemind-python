n=int(input())
a=list(map(int,input().split()))
d=set(a)
c=list(d)
count=0
for i in c:
    if i%2!=0:
        count=count+1
        
print(count)