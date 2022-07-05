n=input()
k="a,e,i,o,u"
p=0
for i in k:
    if i!=",":
        
        if i not in n:
            
            p+=1
##print(p)
if p==0:
    print("True")
else:
    print("False")