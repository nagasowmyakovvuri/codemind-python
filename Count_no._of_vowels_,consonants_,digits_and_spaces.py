a=input()
c=0
d=0
g=0
f=0
for i in a:
    if i in "a,e,i,o,u,A,E,I,O,U":
        c=c+1
    else:
        if i not in "1234567890 ":
            
            f+=1
for i in a:
    if i in"1234567890":
        g=g+1
    if i==" ":
        d+=1
print("Vowels:",c)
print("Consonants:",f)
print("Digits:",g)
print("White spaces:",d)