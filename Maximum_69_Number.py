n=int(input())
n=str(n)
h=0
for i in n:
    if int(i)==6 and h==0:
        print(9,end='')
        h=1
    else:
        print(i,end='')
    