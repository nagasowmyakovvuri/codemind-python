n=input()
l=n.split(' ')
s='aeiou'
k=0
d='bcdfghjklmnpqrstvwxyz'
for i in l:
    p=[]
    for j in range(len(i)//2+1):
        if (i[j] in s and i[len(i)-1-j] in d)or (i[j] in d and i[len(i)-1-j] in s):
            if i[j] not in p or i[len(i)-1-j] not in p:
                p.append(i[j])
                p.append(i[len(i)-1-j])
                k+=1
print(k)