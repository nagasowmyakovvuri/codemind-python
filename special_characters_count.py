a=input()
c=0
p=0
l=0
k=0
s=0
#print(ord("."))
for i in a:
    if ord(i)>=65 and ord(i)<=90:
        c=c+1
    elif ord(i)>=97 and ord(i)<=122:
        p=p+1
    elif i==' ':
        k+=1
    elif i in "0123456789":
        s+=1
    else:
        l=l+1
    
print(l)