n=int(input())
import math
l=n
k=l*l
s=len(str(n))
while(k!=0):
    r=k%pow(10,s)
    if r==n:
        print("Automorphic Number")
        break
    k=k//10
else:
    print("Not an Automorphic Number")