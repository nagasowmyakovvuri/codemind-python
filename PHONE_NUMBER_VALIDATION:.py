n=int(input())
s=0
k=n
while n!=0:
    r=n%10
    s=s+1
    n=n//10
if s==10 and k%int(pow(10,10))!=0:
    print("Valid")
else:
    print("Invalid")