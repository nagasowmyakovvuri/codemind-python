n=int(input())
l=list(map(int,input().split()))
k,m=map(int,input().split())
s=[]
p=0
for i in l:
    if i<k or i>m:
        print(i,end=' ')
        p+=1
if p==0:
    print('-1')