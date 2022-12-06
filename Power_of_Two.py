k=int(input())
for i in range(1,k):
    if pow(2,i)>k:
        print("False")
        break
    if pow(2,i)==k:
        print("True")
        break
else:
    print("False")
