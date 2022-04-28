a=int(input())
count=0
p=0
while a!=0:
    r=a%10
    if r%2==0:
        count+=1
    else:
        p+=1
    a=a//10
if count==0:
    print("Odd")
elif p==0:
    print("Even")
else:
    print("Mixed")