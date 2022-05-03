n=int(input())
flag=0
for i in range(2,n):
    if(i*i==n):
        flag=1
if flag==1:
    print("True")
else:
    print("False")