n=input()
res = [n[i: j] for i in range(len(n))
          for j in range(i + 1, len(n) + 1)]
k=[]
for i in res:
    p=0
    for j in i:
        if i.count(j)==1:
            if ord(j)>=65 and ord(j)<=91:
                if i.count(chr(ord(j)+32))==0:
                    p+=1
            else:
                if i.count(chr(ord(j)-32))==0:
                    p+=1
    if (p==len(i) and len(i)>=3):
        k.append(i)
       
#print(k)
if len(k)>0:
    o=[]
    for i in k:
        o.append(len(i))
    h=max(o)
    for i in k:
        if len(i)==h:
            print(i)
            break
else:
    print("-1")