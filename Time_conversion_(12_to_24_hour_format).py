n=input()
#print(int(n[0]+n[1]))
if n[6]=="A" and n[7]=="M":
    if n[0]=='1' and n[1]=='2':
        print("00:"+n[3]+n[4])
    else:
        print(n[0]+n[1]+n[2]+n[3]+n[4])
else:
    if n[0]=="1" and n[1]=="2":
        print("12:"+n[3]+n[4])
    else:
        print(str(int(n[0])+1)+str(int(n[1])+2)+n[2]+n[3]+n[4])