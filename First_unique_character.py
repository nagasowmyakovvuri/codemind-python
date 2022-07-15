n=input()
s=''
n=n.lower( )
p=0
for i in n:
    if n.count(i)==1:
        print(i)
        p+=1
        break
if p==0:
    print('-1')