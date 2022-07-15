n=input()
s=''
n=n.lower( )
p=0
s=''
for i in n:
    if n.count(i)==1:
        if i not in s and i !=' ':
            p+=1
            s+=i
print(p)
