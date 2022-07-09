n=int(input())
l=list(map(int,input().split()))
k,c=map(int,input().split())
p=0
for i in l:
    if i>=k and i<=c:
        print(i,end=' ')
        p+=1
if p==0:
    print('-1')