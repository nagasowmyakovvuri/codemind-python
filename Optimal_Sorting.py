n=int(input())
while n!=0:
    k=int(input())
    l=list(map(int,input().split()))
    c=0
    for i in range(len(l)-1):
        if(l[i]<=l[i+1]):
            continue
        else:
            c+=1
    if c==0:
        print("0")
    else:
        print(max(l)-min(l))
    n-=1