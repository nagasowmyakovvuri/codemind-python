n= int (input())
a=list(map(int,input().split()))
d=set(a)
c=list(d)
##print(a)
##print(c)
count=0
for i in c:
   ##if i%2!=0 and i!=0:
    count=count+i
        
print(count)