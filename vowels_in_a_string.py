n=input()
k=input()
p=0
for i in range(len(n)):
    if n[i]==k:
        print("True")
        print(i)
        p+=1
        break
if p==0:
    print("False")
        