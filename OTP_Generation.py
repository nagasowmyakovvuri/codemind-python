n=input()
k=int(n)
l=''
while k!=0:
    r=k%10
    if r%2!=0:
        l+=str(r)
    k=k//10
o=l[: :-1]
j=''
##print(o)
for i in o:
    j+=str(int(i)*int(i))
print(j)