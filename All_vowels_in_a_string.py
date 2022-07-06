n=input()
l='aeiou'
k=0
for i in l:
    if i not in n:
        k+=1
if k==0:
    print("True")
else:
    print("False")