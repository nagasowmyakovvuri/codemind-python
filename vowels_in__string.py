n=input()
a='aeiouAEIOU'
p=[]
for i in n:
    if i in a:
        if i not in p:
           p.append(i)
        
if len(p)==0:
    print('-1')
else:
    print(*p)