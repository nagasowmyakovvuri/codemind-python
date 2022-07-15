n=input()
s=''
n=n.lower( )
for i in n:
    if i not in s and i!=' ':
        s+=i
s=list(s)
s.sort( )
l=''
for i in s:
    l+=i
print(len(l))