n=input()
p=0
for i in range(len(n)):
    if n.count(n[i])==1:
        print(i)
        p+=1
        break
if p==0:
    print('-1')