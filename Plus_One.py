n=int(input())
a=list(map(int,input().split()))
k=''
for i in a:
    k+=str(i)
g=int(k)
g=g+1
k=[]
while g!=0:
    r=g%10
    k.append(r)
    g=g//10
k.reverse()
print(*k)