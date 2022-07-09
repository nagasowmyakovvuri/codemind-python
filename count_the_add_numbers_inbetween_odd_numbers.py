n=int(input())
l=list(map(int,input().split()))
p=0
for i in range(len(l)-2):
    if (l[i]%2!=0 and l[i+2]%2!=0):
        if l[i+1]%2!=0:
            p+=1
        
print(p)