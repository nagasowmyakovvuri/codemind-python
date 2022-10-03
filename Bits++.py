n=int(input())
k=0
while n!=0:
    s=input()
    
    if s=="++X" or s=="X++":
        k+=1
    else:
        k-=1
    n-=1
print(k)