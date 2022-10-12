n=input().lower( )
m=input().lower()
s=''
for i in n:
    if i in m:
        if i not in s and i!=" ":
            s+=i
s=list(s)
s.sort()
j=""
for i in s:
    j+=i
if len(s)!=0:
    print(j)
else:
    print('-1')