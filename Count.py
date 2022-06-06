n=int(input())
a=list(map(int,input().split()))
k=0
l=0
for i in a:
    if i%2==0:
        k+=1
    else:
        l=l+1
print(k,l)