n=int(input())
min=0
while n!=0:
    r=n%10
    if r>min:
        min=r
    n=n//10
print(min)