n=int(input())
l=list(map(int,input().split()))
h=set(l)
for i in h:
     if l.count(i)>1:
         print(i)