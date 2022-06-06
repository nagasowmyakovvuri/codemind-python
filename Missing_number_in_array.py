n=int(input())
while n!=0:
    a=int(input())
    b=list(map(int,input().split()))
    sub=[]
    for j in range(1,a+1):
        sub.append(j) 
    ##print(sub)
    for i in sub:
        if i not in b:
            print(i)
    n-=1
        