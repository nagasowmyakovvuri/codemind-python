n=int(input())
l=list(map(int,input().split()))
k=0
for i in l:
    k+=i
o=k/n
print("%.2f"%o)