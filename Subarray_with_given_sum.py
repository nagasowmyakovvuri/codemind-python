n=int(input())
while n!=0:
    k,m=map(int,input().split())
    l=list(map(int,input().split()))
    p=0
    h=0
    for i in range(0,k):
        #s=0
        p=0
        for j in range(0,k):
            s=0
            for c in range(i,j+1):
                s+=l[c]
               # print(l[c],end=" ")
                
                if(s==m):
                    print(i+1,j+1)
                    p=1
            if p==1:
                break
                #else:
            #print()   
        if p==1:
                h=1
                break
        
    if h==0:
        print('-1')
    n-=1
    