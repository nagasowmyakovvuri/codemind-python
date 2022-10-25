m=input()
n=int(input())
k=m.count('a')
l=n//len(m)
h=n%len(m)
p=0
for i in range(0,h):
    if m[i]=='a':
        p+=1
print(k*(l)+p)