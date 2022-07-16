n=int(input())
l=list(map(int,input().split()))
m=[]
for i in range(len(l)//2):
    m.append(l[i])
    m.append(l[len(l)-1-i])
if len(l)%2==0:
    print(*m)
else:
    m.append(l[(len(l)//2)])
    m.append('0')
    print(*m)