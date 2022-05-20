def is_prime(n):
    for i in range(2,n):
        if(n%i==0):
            return 0
    return 1
def palindrome(n):
   i=1
   while(1):
       k=n+i
       l=k
       s=0
       r=0
       while(k!=0):
           r=k%10
           s=s*10+r
           k=k//10
        
       if(l==s):
            if(is_prime(l)):
                return l
       i=i+1

n=int(input())
print(palindrome(n))