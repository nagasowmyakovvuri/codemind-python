n=int(input())
flag=0
s=0
count=0
k=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    flag=1
while n!=0:
    r=n%10
    s=s+1
    p=0
    for j in range(1,r+1):
        if r%j==0:
            p=p+1
    if p==2:
        k=k+1
    n=n//10
if flag==1 and s==k:
    print("Mega Prime")
else:
    print("Not Mega Prime")