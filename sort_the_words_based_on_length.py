n=input()
k=n.split()
l=list(sorted(k,key=len))

#print(l)
for i in range(0,len(l)-1):
    if l[i]>l[i+1] and len(l[i])==len(l[i+1]):
        p=l[i]
        l[i]=l[i+1]
        l[i+1]=p
    else:
        i+=1
print(" ".join(l))