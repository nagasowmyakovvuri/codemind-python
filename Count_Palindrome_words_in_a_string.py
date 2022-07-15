n=input().lower( )
l=n.split(' ')
p=0
for i in l:
   k=i[::-1]
   if i==k:
       p+=1
print(p)
    