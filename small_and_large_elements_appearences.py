n=input()
k=''
for i in n:
    if i!=' ':
        k+=i
    else:
        continue
print(min(k),k.count(min(k)),max(k),k.count(max(k)))