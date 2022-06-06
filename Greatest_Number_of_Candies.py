n=int(input())
a=list(map(int,input().split()))
k=int(input())
m=max(a)
for i in range(0,len(a)):
    s=0
    h=0
    s=a[i]+k
    if s>=m:
        h+=1
    if h>0:
        print("True",end=' ')
    else:
        print("False",end=' ')