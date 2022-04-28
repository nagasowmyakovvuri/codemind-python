n=int(input())
s=0
k=1
while n!=0:
    r=n%10
    s=s+r
    k=k*r
    n=n//10
    
if(s==k):
    print("Spy Number")
else:
    print("Not Spy Number")