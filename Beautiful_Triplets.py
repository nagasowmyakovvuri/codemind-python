n=int(input())
l=list(map(int,input().split()))
while len(l)!=0:
    k=min(l)
    j=[]
   # print(k)
    print(len(l))
    for i in l:
        if i>k:
            j.append(i-k)
    #print(j)
    
    l=j