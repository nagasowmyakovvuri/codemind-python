a=input()
c=0
for i in a:
    if i in "aeiouAEIOU":
        c=c+1
    if i==" ":
        print(c,end=' ')
        c=0
else:
    print(c)