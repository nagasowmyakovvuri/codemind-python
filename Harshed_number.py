n=int(input())
s=n
sum=0
while n!=0:
    r=n%10
    sum=sum+r
    n=n//10
if s%sum==0:
    print("True")
else:
    print("False")