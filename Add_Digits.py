n=int(input())
s=0
k=n
while k>=10:
     s=0
     r=0
     while(n!=0):
         r=n%10
         s=s+r
         n=n//10
     k=s
     n=s
print(s)