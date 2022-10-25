n=input()
#print(int(n[0]+n[1]))
if n[0]=='0' and n[1]=='0':
    print("12:"+n[3]+n[4]+" AM")
elif int(n[0]+n[1])<12:
    print(n[0]+n[1]+n[2]+n[3]+n[4]+" AM")
elif int(n[0]+n[1])==12:
    print(n+" PM")
else :
    print(str(int(n[0])-1)+str(int(n[1])-2)+n[2]+n[3]+n[4]+" PM")
