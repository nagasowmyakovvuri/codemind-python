def binary(n):
    if n==0:
        return "000"
    elif n==1:
        return "001"
    elif n==2:
        return "010"
    elif n==3:
        return "011"
    elif n==4:
        return "100"
    elif n==5:
        return "101"
    elif n==6:
        return "110"
    elif n==7:
        return "111"
        
k=int(input())
d=str(k)
g=""
for i in d:
    g+=binary(int(i))
print(int(g))
    