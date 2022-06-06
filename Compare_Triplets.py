a,b,c=map(int,input().split())
l,k,h=map(int,input().split())
#print(a,b,c)
#print(l,k,h)
s=0
p=0
i=0
if a>l:
    s+=1
if a<l:
    p+=1
if b<k:
    p+=1
if b>k:
    s+=1
if c>h:
    s+=1
if c<h:
    p+=1
print(s,p)