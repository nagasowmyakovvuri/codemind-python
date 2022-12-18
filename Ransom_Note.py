n,m=map(str,input().split())
p=0
for i in n:
    if m.count(i)>=n.count(i) and i in n:
        p+=1
        #print(i)
if p==len(n):
    print("True")
else:
    print("False")