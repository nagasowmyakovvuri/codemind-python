n=int(input())
a=2
b=2
s=0
k=[]
for i in range(n):
    k.append(a)
    s=a+b
    a=b
    b=s
print(k[n-1])
    
    