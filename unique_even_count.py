n=int(input())
a=list(map(int,input().split()))
c=set(a)
count=0
d=list(c)
for i in d:
    if(i%2==0):
        count+=1
print(count)