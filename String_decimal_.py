n=int(input())
while n!=0:
    a=input()
    f=0
    ##print(a)
    for i in a:
        if i not in "1234567890":
            f+=1
    if f==0:
        print("True")
    else:
        print("False")
    n-=1