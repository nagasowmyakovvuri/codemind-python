n=input()
a='a,e,i,o,u,A,E,I.O,U'
k=0
for i in n:
    if i in a:
        k+=1
print(k)