n=int(input())
arr=list(map(int,input().split()))
sub_lists= [[]] 
l=[]
for i in range(len(arr) + 1): 
    for j in range(i + 1, len(arr) + 1): 
        sub = arr[i:j] 
        sub_lists.append(sub) 
for i in sub_lists:
    k=0
    for j in i:
        k+=j
    if len(i)>=1:
        l.append(k)
print(max(l))