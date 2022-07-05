n=input()
l=n.split(' ')

k=min(l[len(l)-1])
##print(chr(ord(k)+32))
if chr(ord(k)+32) in n:
    print(chr(ord(k)+32))
else:
    print(k)