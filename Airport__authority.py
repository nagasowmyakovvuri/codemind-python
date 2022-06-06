a=int(input())
k=[]
while a!=0:
    h=int(input())
    k.append(h)
    a=a-1
g=int(input())
s=0
for i in k:
    if i<=g:
        s=s+1
    else:
        s=s+2
print(s)