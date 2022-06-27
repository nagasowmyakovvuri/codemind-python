n=int(input())
l=list(map(int,input().split()))
k=0
o=0
for i in range(len(l)//2):
    k+=l[i]
for i in range(len(l)//2,len(l)):
    o+=l[i]
print(abs(k-o))