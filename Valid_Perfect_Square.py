n=int(input())
flag=0
while n!=0:
    flag=0
    k=int(input())
    for i in range(1,k):
        if(i*i==k):
            flag=1
    if flag==1:
        print("True")
    else:
        print("False")
    n=n-1