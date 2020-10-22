import math
print('This is Newton Raphson Method') 

def func(x):
    return x**4-7*x**3+2*x**2+3*x+3
def fd(a):
    if abs(a)>0.01:
        t=0.01*abs(a)
    else:
        t=0.0001
    d=(func(a+t)-func(a-t))/(2*t)
    return d
def fdd(a):
    if abs(a)>0.01:
        t=0.01*abs(a)
    else:
        t=0.0001
    d=(func(a+t)-(2*func(a))+func(a-t))/(math.pow(t,2))
    return d
x0=float(input("enter the initial value of x: "))
e=float(input("enter termination parameter: "))
k=0
y1=fd(x0)
y2=fdd(x0)
x1=x0-(y1/y2)
y3=fd(x1)
k=k+1
x0=x1
y1=fd(x0)
y2=fdd(x0)
x1=x0-(y1/y2)   
while abs(y3)>e:
    k=k+1
    x0=x1
    y1=fd(x0)
    y2=fdd(x0)
    x1=x0-(y1/y2)
    y3=fd(x1)
print("min value is {}".format(x0))
