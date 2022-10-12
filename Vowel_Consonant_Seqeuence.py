n=input()
s=""
for i in n:
    if i not in"aeiou":
        if len(s)==0:
            s+="C"
        else:
            if(s[len(s)-1]!="C"):
                s+="C"
    else:
        if len(s)==0:
            s+="V"
        else:
            if(s[len(s)-1]!="V"):
                s+="V"
print(s)
        