n=int(input())
l=list(map(int,input().split()))
p=0
d=0
##print(l)
for i in range(0,len(l)-2,2):
    if (l[i]<l[i+1] and l[i+1]>l[i+2]) or (l[i]>l[i+1] and l[i+1]<l[i+2]):
        p+=1
    else:
        d+=1
    ##print(l[i],l[i+1],l[i+2])
    
if d==0:
    print('yes')
else:
    print('no')
