n=input()
l=input()
d=l.split(' ')
n=n.lower()
l=l.lower()
k=n.split(' ')
j=l.split(' ')
for i in range(len(j)):
    if j[i] in k:
        print(d[i],end=' ')