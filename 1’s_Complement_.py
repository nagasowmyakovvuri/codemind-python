n=int(input())
l=bin(n)
p=l.replace('0b','')
k=""
for i in p:
    if i=='1':
        k+='0'
    else:
        k+='1'
j=0
for  i in range(len(k)-1,-1,-1):
    j+=int(k[i])*pow(2,len(k)-i-1)
print(j)