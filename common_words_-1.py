n=input()
l=input()
p=n.lower()
j=l.lower()
p=p.split(' ')
j=j.split(' ')
o=0
for i in p:
    if i in j:
        o+=1
print(o)