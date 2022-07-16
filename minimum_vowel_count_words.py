n=input()
k=n.split(' ')
s='aeiou'
p=[]
for i in k:
    i=i.lower()
    d=0
    for j in i:
        if j in s:
            d+=1
    p.append(d)
l=0
for i in k:
    i=i.lower()
    d=0
    for j in i:
        if j in s:
            d+=1
    if d==min(p):
        l+=1
print(l)