n=input()
s=''
n=n.lower( )
for i in n:
    if n.count(i)==1 and i!=' ':
        s+=i
s=list(s)
s.sort( )
l=''
for i in s:
    l+=i
print(l)