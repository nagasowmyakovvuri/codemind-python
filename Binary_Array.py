n=int(input())
l=list(map(int,input().split()))
p=0
for i in l:
    if str(i) not in '01':
        p+=1
if p==0:
    print("True")
else:
    print("False")
        
        