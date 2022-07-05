n=input()
k=0
f=n.split()
g="a,e,i,o,u,A,E,I,O,U"
for i in f:
    k=0
    for j in i:
        
        if j in g:
           k+=1
    print(k,end=' ')