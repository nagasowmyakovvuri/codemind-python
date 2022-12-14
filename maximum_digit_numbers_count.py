n=int(input())
l=list(map(int,input().split()))
k=[]
p=[]
for i in l:
    p.append(len(str(i)))
o=max(p)
for i in l:
    if len(str(i))==o:
        print(i,end=" ")