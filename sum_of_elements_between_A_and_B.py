n=int(input())
l=list(map(int,input().split()))
k,v=map(int,input().split())
s=0
for i in l:
    if i>=k and i<=v:
        s+=i
print(s)