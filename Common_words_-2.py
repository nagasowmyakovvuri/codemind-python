s=input()
k=input()
m=s.split()
n=k.split()
#print(s)
#print(k)
p=0
for i in m:
    o=m.count(i)
    j=n.count(i)
    #print(o)
    if i in n and o==1 and j==1:
        p+=1
print(p)