n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if i not in k:
        k.append(i)
k.sort()
k.reverse()
if len(k)>2:
   print(k[2])
else:
   print(k[0])