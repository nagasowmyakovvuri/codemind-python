n=input()
res = [n[i: j] for i in range(len(n))
          for j in range(i + 1, len(n) + 1)]
m=[]
k=[]
p=0
#print(res)
for i in res:
    p=0
    for j in i:
        if j not in 'aeiou':
            p+=1
    if p==0:
        m.append(i)
d=[]
for i in m:
    d.append(len(i))
print(max(d))