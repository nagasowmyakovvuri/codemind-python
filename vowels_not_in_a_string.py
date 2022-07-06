n=input()
l='aeiou'
p=0
for i in l:
    if i not in n:
        print(i,end=' ')
        p+=1
if p==0:
    print("0")