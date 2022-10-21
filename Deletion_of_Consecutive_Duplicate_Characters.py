k=int(input())
while k!=0:
    n=input()
    l=0
    for i in range(0,len(n)-1):
        if(n[i]==n[i+1]):
            l+=1
    print(l)
    k-=1