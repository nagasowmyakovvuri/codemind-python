n=int(input())
k=n
d=0
s=n
sum=0
while n!=0:
    d=d+1
    n=n//10
while k!=0:
    r=k%10
    sum=sum+pow(r,d)
    k=k//10
    d=d-1
if sum==s:
    print("True")
else:
    print("False")