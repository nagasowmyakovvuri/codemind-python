n=int(input())
l=list(map(int,input().split()))
s=len(l)-1
k=0
for i in l:
    k=k+i*(pow(2,s))
    s=s-1
print(k)