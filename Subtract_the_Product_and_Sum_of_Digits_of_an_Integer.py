a=int(input())
sum=0
p=1
while a!=0:
    r=a%10
    sum=sum+r
    p=p*r
    a=a//10
k=p-sum
print(k)