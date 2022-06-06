a=int(input())
n=list(map(int,input().split()))
k=0
l=0
for i in range(0,a):
    if i%2==0:
        k+=n[i]
    else:
        l+=n[i]
s=k-l
if s>=0:
    h=abs(s)
    if h%4==0:
        print("X")
    else:
        print("Y")
else:
    if s%4==0:
        print("X")
    else:
        print("Y")