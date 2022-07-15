n=input()
l=n.split(' ')
k=min(l[len(l)-1])
f=k.lower( )
if f in l[len(l)-1]:
    print(f)
else:
    print(k)