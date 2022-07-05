n=input()
l=n.split(' ')
for i in range(len(l)-1,-1,-1):
    k=l[i]
    print(k[::-1],end=' ')