n=int(input())
a=[list(map(int,input().strip().split()))for i in range(n)]
s=0
p=0
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            s=s+a[i][j]
        if i==n-j-1:
            p+=a[i][j]
f=""
f+="Principal Diagonal:"
f+=str(s)
print(f)
g=""
g+="Secondary Diagonal:"
g+=str(p)
print(g)
        

