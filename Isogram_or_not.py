n=input()
k=0
for i in n:
    if n.count(i)!=1:
        k+=1
if k==0:
    print("True")
else:
    print("False")