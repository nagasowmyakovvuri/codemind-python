n=input().lower( )
d=[]
l=n.split(' ')
for i in l:
    p=0
    for j in i:
        if j in 'aeiou':
            p+=1
    d.append(p)
print(min(d))