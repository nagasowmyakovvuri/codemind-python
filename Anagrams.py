n=input().lower()
l=input().lower()
p=0
for i in n:
    if i not in l:
        p+=1
if p==0:
    print('True')
else:
    print("False")