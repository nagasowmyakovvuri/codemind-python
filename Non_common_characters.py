n=input().lower( )
l=input().lower( )
p=[]
for i in n:
    if i not in l and i!=' ' and i not in p:
        p.append(i)
for i in l:
    if i not in n and i!=' ' and i not in p:
        p.append(i)
print(len(p))