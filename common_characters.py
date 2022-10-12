n=input().lower()
m=input().lower()
s=""
for i in n:
    if i in m:
        if i not in s and i!=" ":
            s+=i
l=list(s)
l.sort()
k=""
for i in l:
    k+=i
if len(k)>0:
    print(k)
else:
    print("-1")