n=int(input())
l=list(map(int,input().split()))
k=min(l)
for i in range(1,k+1):
    h=0
    for j in l:
        if j%i==0:
            h+=1
    if h==len(l):
       hcf=i
print(hcf)
            