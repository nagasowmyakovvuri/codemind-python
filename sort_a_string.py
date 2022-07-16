n=input()
k=''
p=[]
j=''
d=[]
h=0
g=0
for i in range(len(n)):
    if n[i] in ' !@#$%^&*(){}[]':
        p.append(i)
        j+=n[i]
    else:
        k+=n[i]
k=list(k)
k.sort( )
for i in range(len(n)):
    if i in p:
        d.append(j[h])
        h+=1
    else:
        d.append(k[g])
        g+=1
for i in d:
    print(i,end='')