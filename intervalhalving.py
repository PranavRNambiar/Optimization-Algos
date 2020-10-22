import math
print('This is Interval Halving Method') 

def func(x):
    return x*x+54/x
a=int(input("enter the first point in interval"))
b=int(input("enter the second point in interval"))
e=float(input("enter termination parameter"))
l=b-a
while abs(l)>=e:
    xm=(a+b)/2
    ym=func(xm)
    x1=a+(l/4)
    x2=b-(l/4)
    y1=func(x1)
    y2=func(x2)
    if y1<ym:
        b=xm
        xm=x1
    elif y2<ym:
        a=xm
        xm=x2
    else:
        a=x1
        b=x2
    l=b-a
print("minimum lies in between {} and {}".format(a,b))
 
 
