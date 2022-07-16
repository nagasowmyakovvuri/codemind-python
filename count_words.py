n=input().lower()
l=n.split(' ')
s='aeiou'
h='bcdfghjklmnpqrstvwxyz'
p=0
for i in l:
    if i[0] in s and i[len(i)-1] in h:
        p+=1
print(p)