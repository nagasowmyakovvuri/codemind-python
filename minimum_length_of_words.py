n=input()
l=n.split(' ')
k=[]
for i in l:
    k.append(len(i))
print(min(k))