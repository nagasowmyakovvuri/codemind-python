n=input().lower( )
l=n.split(' ')
s=''
for i in l[0]:
    k=0
    for j in range(1,len(l)):
        if i in l[j]:
            k+=1
    if k==len(l)-1:
        s+=i
if len(s)!=0:
    print(s)
else:
    print('-1')