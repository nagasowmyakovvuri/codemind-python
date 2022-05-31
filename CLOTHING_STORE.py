n=int(input())
a=list(map(int,input().split()))
c=0
p=0
for i in range(0,n):
    if a[i]!=-1:
        c=1
        for j in range(0,n):
            if a[i]==a[j] and i!=j:
                c+=1
                a[j]=-1
        p+=c//2
print(p)
                