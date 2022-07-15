n=input()
l=n.split(' ')
s=[]
for i in l:
    k=ord(max(i))-ord(min(i))
    s.append(k)
print(*s)