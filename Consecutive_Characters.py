n=input()
res = [n[i: j] for i in range(len(n))
          for j in range(i + 1, len(n) + 1)]
l=[]
k=[]
for i in res:
    if i==i[::-1]:
        l.append(i)
for i in l:
    p=""
    for j  in i:
        if j not in p:
            p+=j
    if len(p)==1:
        
        k.append(len(i))
print(max(k))