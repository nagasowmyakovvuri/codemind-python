n=int(input())
while n!=0:
    k=int(input())
    o=str(k)
    o=list(o)
    l=[]
    for i in o:
        l.append(int(i))
    l.sort()
  #  print(l)
    for i in range(0,len(l)-1):
        if l[i]!=l[i+1]-1:
            print("NO")
            break
    else:
        print("YES")
    n-=1