n=int(input())
l=list(map(int,input().split()))
p=0

for i in range(len(l)-1):
    if l[i]>=l[i+1]:
        p+=1
if p==0:
    print("yes")
else:
    print("no")