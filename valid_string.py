n=input()
k=""
l=[]
for i in n:
    if i not in k:
         k+=i
for i in k:
    l.append(n.count(i))
o=l[0]
m=0
for i in range(1,len(l)):
    if l[i]!=o:
        m+=1
if m>1:
    print("Not Valid")
else:
    print("Valid String")