a=input()
c=0
s=' '
f=1
p=0
for i in a:
    if i in "aeiouAEIOU":
        c=c+1
    if i==" ":
        s+=str(c)
        c=0
        p=1
if p==0:
    print(c)
    f=0
if f==1:
       print(max(s))