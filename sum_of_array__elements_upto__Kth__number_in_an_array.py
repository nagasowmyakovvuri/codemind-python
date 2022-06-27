n=int(input())
l=list(map(int,input().split()))
d=int(input())
k=0
for i in l:
    if i==d:
        k+=i
        break
    else:
        k+=i
print(k)
    