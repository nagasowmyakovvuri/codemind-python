n=int(input())
l=list(map(int,input().split()))
p=0
h=0
for i in range(len(l)):
    if i%2==0:
        if l[i]%2==0:
            p+=1
    if l[i]%2==0:
        h+=1
if p==h:
    print("True")
else:
    print("False")