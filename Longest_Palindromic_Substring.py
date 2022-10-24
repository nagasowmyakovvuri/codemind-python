n=input()
res = [n[i: j] for i in range(len(n))
          for j in range(i + 1, len(n) + 1)]
l=[]
k=[]
for i in res:
    if i==i[::-1]:
        l.append(i)
for i in l:
    k.append(len(i))
s=max(k)
for i in l:
    if len(i)==s:
        print(i)
        break