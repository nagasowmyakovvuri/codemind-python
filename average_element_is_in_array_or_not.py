n=int(input())
l=list(map(int,input().split()))
k=0
for i in l:
    k+=i
o=k//n
if o in l:
    print("True")
else:
    print("False")
