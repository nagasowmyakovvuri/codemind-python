d=input()
f=input()
s=[]
g=[]
for i in d:
    if i!="#":
        s.append(i)
    else:
        s.remove(s[len(s)-1])
for i in f:
    if i!="#":
        g.append(i)
    else:
        g.remove(g[len(g)-1])
if s==g:
    print("True")
else:
    print("False")