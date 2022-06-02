a=input()
p=input()
for i in range(len(a)):
    if a[i]==p:
        print("True")
        print(i)
        break;
else:
    print("False")