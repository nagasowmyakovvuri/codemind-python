def is_prime(a):
    for i in range(2,(a//2)+1):
        if a%i==0:
            return 0
    if a==1:
        return 0
    return 1
    
n=int(input())
a=list(map(int,input().split()))
m=min(a)
n=max(a)
for i in range(0,n):
    if a[i]==m:
        k=i
        break
for i in range(0,n):
    if a[i]==n:
        l=i
        break
if k>l:
   f=l
   last=k
else:
    f=k
    last=l
c=0
for i in range(f,last+1):
    if(is_prime(a[i])==1):
        c+=1
print(c)