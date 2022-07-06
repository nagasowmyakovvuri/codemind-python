n=input()
l=n.split(' ')
for i in range(len(l)):
    if i%2==0:
        j=l[i]
        print(j[::-1],end=' ')
    else:
        print(l[i],end=' ')

    