n=input()
l=n.split(' ')
for i in l:
    a=[]
    s=[]
    d=[]
    u=0
    h=0
    o=[]
    f=''
    for j in range(len(i)):
        if i[j] in 'aeiou':
            s.append(j)
            d.append(i[j])
        else:
            o.append(i[j])
    o.sort()
    for x in range(len(i)):
        if x in s:
            a.append(d[u])
            u+=1
        else:
            a.append(o[h])
            h+=1
    for i in a:
        f+=i
    print(f,end=' ')
        