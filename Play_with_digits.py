n=int(input())
l=list(map(int,input().split()))
s=0
##print(*l)
for i in l:
    r=0
    while i!=0:
        r=i%10
        s=r+s
        i=i//10
print(s)
    