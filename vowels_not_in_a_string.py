n=input()
a='aeiou'
k=''
for i in a:
    if i not in n:
        k+=i
if len(k)==0:
    print("0")
else:
    k=list(k)
    k.sort()
    print(*k)
        