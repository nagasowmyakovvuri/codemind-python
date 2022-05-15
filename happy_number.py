n=int(input())
import math
k=n
while(k>=10):
    sum=0
    r=0
    while(n!=0):
        r=n%10
        sum=pow(r,2)+sum
        n=n//10
    k=sum
    n=sum
if sum==1 or sum==7:
    print("True")
else:
    print("False")