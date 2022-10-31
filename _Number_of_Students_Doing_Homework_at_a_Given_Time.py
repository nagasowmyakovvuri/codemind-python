n=int(input())
l=list(map(int,input().split()))
m=int(input())
k=list(map(int,input().split()))
s=int(input())
p=0
f=[]
for i in range(0,n):
    if k[i]>=s and l[i]<=s:
        p+=1
print(p)