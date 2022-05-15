n=int(input())
import math
##print(n)
k=n*n
l=n
s=0
d=len(str(n))
##print(d)
j=0
while(k!=0):
    ##r=k%10
    ##j=j+1
    ##s=s*10+r
    if k%pow(10,d)==n:
        print("Automorphic Number")
        break
    ##else:
        ##continue
    k=k//10
else:
    print("Not an Automorphic Number")
    