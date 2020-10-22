import math 
print('This is Bisection Method') 

def f(x):
    return x*x+(54/x)
def delta(z):
    if z<-0.01 or z>0.01:
        val=0.01*abs(z)
    else: 
        val=0.0001
    return val
def f_(c):
    return (f(c+delta(c))-f(c-delta(c)))/(2*delta(c))
a=float(input("Enter the lower bound "))
b=float(input("Enter the upper bound "))
choice = input("Do you want to enter the no. of iterations : y/n ")
if choice=='y' or choice == 'Y':
    n=int(input("Enter the no. of iterations "))
    if f_(a)<0 and f_(b)>0:
        x1=a
        x2=b
        while n!=0:
            n=n-1
            z=(x1+x2)/2
            if f_(z)<0:
                x1=z
            else:
                x2=z
            if n==0:
                print(f"Minimum point : {(x1+x2)/2}, Minimum value : {f((x1+x2)/2)}")
    else:
        print("Minimum doesn't exist in the given interval ")
 
else:
    e=float(input("Enter termination parameter "))
    flag=0
    if f_(a)<0 and f_(b)>0:
        x1=a
        x2=b
        while flag==0:
            z=(x1+x2)/2
            if abs(f_(z))<e:
                flag=1
                print(f"Minimum point : {z}, Minimum value : {f_(z)}")
            elif f_(z)<0:
                x1=z
            else:
                x2=z
    else:
        print("Minimum doesn't exist in the given interval ")
