def ugly(a):
    if a==1:
        return 1
    if(a<=0):
        return 0
    if(n%2==0):
        return (ugly(a//2))
    if(n%3==0):
        return ugly(a//3)
    if(n%5==0):
        return ugly(a//5)
    return 0
n=int(input())
if(ugly(n)):
    print("Ugly Number")
else:
    print("Not Ugly Number")