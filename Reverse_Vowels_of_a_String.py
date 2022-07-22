n=input()
k=''
s=[]
d=''
m=[]
for i in range(len(n)):
    if n[i] in 'aeiouAEIOU':
        k+=n[i]
        s.append(i)
    else:
        d+=n[i]
        m.append(i)
k=k[::-1]
x=0
z=0
c=''

for i in range(len(n)):
    if i in s:
        c+=k[x]
        x+=1
    else:
        c+=d[z]
        z+=1
print(c)