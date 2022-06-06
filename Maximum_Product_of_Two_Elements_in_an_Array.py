a=list(map(int,input().split()))
k=[]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        l=(a[i]-1)*(a[j]-1)
        k.append(l)
print(max(k))