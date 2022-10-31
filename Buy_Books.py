n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
k=0
s=0
for i in range(0,n):
    k+=l[i]
    s+=m[i]
p=s-k
if(p>0):
    print(p)
else:
    print('0')