n=input().lower( )
l=input().lower( )
h=[]
for i in n:
    if i in l and i!=' ':
        h.append(i)
h=set(h) 
h=list(h)
print(len(h))