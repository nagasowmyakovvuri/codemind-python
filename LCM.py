a,b=map(int,input().split())
min=a
max=b
if a>b:
    min=b
    max=a
##print(max,min)
i=min
##print(i)
while i>=min:
    ##print(i)
    if i%a==0 and i%b==0:
        
        print(i)
        break
    i=min+i
##print(lcm)