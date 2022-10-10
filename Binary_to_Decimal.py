n=int(input())
while n!=0:
    k=int(input())
    d=str(k)
    j=0
    x=0
    for i in range(len(d)-1,-1,-1):
        x+=pow(2,j)*int(d[i])
        j+=1
    print(x)
    n-=1