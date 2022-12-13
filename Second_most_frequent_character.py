n=input()
p=""
k=[]
for i in n:
    if i not in p and n.count(i) not in k:
        p+=i
        k.append(n.count(i))
#print(k)
if len(k)<=1:
    print("-1")
else:
    k.sort()
    for i in p:
        if n.count(i)==k[len(k)-2]:
            print(i)
            break