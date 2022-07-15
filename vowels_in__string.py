n=input()
d='aeiouAEIOU'
p=0
s=''
for i in n:
    if i in d:
        if i not in s:
            s+=i

if len(s)==0:
    print('-1')
else:
    for i in s:
        print(i,end=' ')