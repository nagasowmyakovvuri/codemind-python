n=int(input())
r=n*n
sum=0
while r!=0:
    k=r%10;
    sum=sum+k
    r=r//10
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")