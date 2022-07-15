n=input()
s=''
p=0
n=n.lower( )
for i in n:
    if n.count(i)==1 and i!=' ':
        p+=1
     
print(p)