import math
def func(x):
    return x*x*x*x+10*x+12-(math.exp(0.2*x))-18
a=int(input("enter the first point in interval:"))
b=int(input("enter the second point in interval:"))
n=int(input("enter the number of  intervals:"))
x1=a
dx=(b-a)/n
x2=x1+dx
x3=x2+dx
while x3<=b:
    if func(x1)>=func(x2) and func(x2)<=func(x3):
        
        break
    else:
        x1=x2
        x2=x3
        x3=x2+dx
if x3>b:
    print("min doesnot exist in interval")
else:
    print("min exists in  the interval",x1, "and",x3)
