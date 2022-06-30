n=int(input())
l=[]
while n!=0:
    r=n%10
    l.append(r)
    n=n//10
k=set(l)
if len(k)==len(l):
    print("Unique Number")
else:
    print("Not Unique Number")