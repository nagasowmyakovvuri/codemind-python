n=int(input())
while n!=0:
    a=input()
    for i in a:
        if i in '1,2,3,4,5,6,7,8,9,0':
            print("Yes")
            ##f=1
            break
    else:
        print("No")
    n=n-1