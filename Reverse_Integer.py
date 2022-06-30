n=int(input())
t=n
if t<0:
    n=abs(n)
s=0
while n!=0:
    r=n%10
    s=s*10+r
    n=n//10
if t<0:
    print(-s)
else:
    print(s)