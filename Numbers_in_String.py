a=input()
c=0
for i in a:
    if i in "1234567890":
        c=c+int(i)
print(c)