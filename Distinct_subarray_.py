n=int(input())
m=int(input())
arr=[]
for i in range(n,m+1):
    arr.append(i)
sub_lists= [[]] 
l=[]
g=0
for i in range(len(arr) + 1): 
    for j in range(i + 1, len(arr) + 1): 
        sub = arr[i:j] 
        sub_lists.append(sub) 
for i in sub_lists:
    p=0
    for j in i:
     
        p+=j
    if p%2!=0:
        g+=1
print(g)
            