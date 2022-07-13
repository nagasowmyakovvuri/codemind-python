n=int(input())
while n!=0:
    l=int(input())
    k=input()
    p=0
    ##print(k)
    for i in k:
        if k.count(i)==1:
            print(i)
            p+=1
            break
    if p==0:
        print('-1')
    n-=1
