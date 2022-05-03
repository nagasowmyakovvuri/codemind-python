a=int(input())
k=int(input())
sum=0
for i in range(1,a):
    if a%i==0:
        sum=sum+i
if sum==k:
    print("Amicable")
else:
    print("Not Amicable")