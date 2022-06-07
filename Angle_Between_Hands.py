def angle(hh,mm):
    v=0
    if(hh<0 or mm<0 or hh>12 or mm>60):
        v=1
    if(hh==12):
        hh=0
    if mm==60:
        mm=0
    hour=0.5*(h*60+m)
    minute=6*m
    angle=abs(hour-minute)
    angle=min(360-angle,angle)
    return angle
h,m=map(int,input().split(':'))
print(angle(h,m))