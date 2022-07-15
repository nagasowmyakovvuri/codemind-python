n=input()
k=n.split(' ')
s='aeiou'
p=[]
for i in k:
    i=i.lower()
    k=0
    for j in i:
        if j in s:
            k+=1
    p.append(k)
print(min(p))