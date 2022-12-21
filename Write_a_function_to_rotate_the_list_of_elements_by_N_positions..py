n=int(input())
l=list(map(int,input().split()))
pos=int(input())
k=[]
s=[]
for i in l:
    k.append(i)
for i in l:
    k.append(i)
if(pos>n):
    pos=pos%n
for i in range(n-pos,2*n-pos):
    if i!=2*n-pos-1:
        print(k[i],end=" ")
    else:
        print(k[i],end="")