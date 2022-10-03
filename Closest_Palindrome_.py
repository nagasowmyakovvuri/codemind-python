def is_palindrome(a):
    r=0
    s=0
    l=a
    while(a!=0):
        r=a%10
        s=s*10+r
        a=a//10
    if l==s:
        return 1
    return 0
n=int(input())
i=n+1
j=n-1
k=0
while(1):
    if is_palindrome(j)==1:
       print(j,end=' ')
       k=k+1
    if is_palindrome(i)==1:
        print(i)
        k=k+1
    if(k>0):
        break
    i=i+1
    j=j-1