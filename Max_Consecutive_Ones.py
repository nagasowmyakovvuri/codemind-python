a=int(input())
b=list(map(int,input().split()))
k=0
#print(b)
s=[]
for i in range(a):
    if b[i]==0:
        k=0
    if b[i]==1:
        k+=1
    s.append(k)
print(max(s))