n=int(input())
k=n
sum=0
p=1
while n!=0:
    r=n%10
    p=1
    for i  in range(1,r+1):
        p=p*i
    sum=sum+p
    n=n//10
if k==sum:
    print("The number",k,"is a strong number")
else:
    print("The number",k,"is not a strong number")