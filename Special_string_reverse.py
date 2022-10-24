n=input()
k=[]
j=[]
s=[]
for i in range(len(n)):
    if ord(n[i])>=65 and ord(n[i])<=91 or ord(n[i])>=92 and ord(n[i])<=122:
        k.append(n[i])
    else:
        j.append(n[i])
        s.append(i)
k.reverse()
#print(k)
b=""
o=0
h=0
for i in range(0,len(n)):
    if i  in s:
        b+=j[o]
        o+=1
        #print(j[o])
    else:
        b+=k[h]
        h+=1
print(b)