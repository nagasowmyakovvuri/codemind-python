a=input()
s=0
for i in a:
    if i in '1234567890':
        s=s+int(i)
print(s)