n=input()
l='!@#$%^&*():"?/><.\,|;'
k=0
a=[]
o=[]
g=[]
s=[]
for i in n:
    if i in l:
        k+=1
for i in n:
    if i in'0123456789':
        s.append(int(i))
for i in s:
    if i%2==0:
        o.append(i)
    else:
        g.append(i)
i=0
j=0

if k%2==0:
    while(i<len(o) and j<len(g)):
        a.append(o[i])
        a.append(g[j])
        i+=1
        j+=1
    while j<len(g):
        a.append(g[j])
        j+=1
    while i<len(o):
        a.append(o[i])
        i+=1
else:
    while(i<len(o) and j<len(g)):
        a.append(g[i])
        a.append(o[j])
        i+=1
        j+=1
    while i<len(o):
        a.append(o[i])
        i+=1
    while j<len(g):
        a.append(g[j])
        j+=1
p=''
for i in a:
    p+=str(i)
print(p) 