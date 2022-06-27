n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
k=0
a=set(a)
b=set(b)
j=[]
for i in a:
    if i  not in b:
        k+=1
        j.append(i)
for i in b:
    if i not in a and i not in j:
        k+=1
print(k)