import math
print('This is Boundiing Phase Method') 

def func(x):
    return math.pow(x,4)+10*x*x+x-math.exp(0.2*x)
def find(delta,x0):
    k=0;
    while(True):
        x1=x0+(2**k)*delta
        if(func(x1)<func(x0)):
            k+=1
            x0=x1
        else:
            print("the range is between {} and {}".format(x1-delta*(3*2**(k-1)),x1))
            break
            
            
while(True):
    delta=float(input("enter the delta value"))
    x0=float(input("enter the intial point value of x"))
    if(func(x0-delta)>=func(x0)>=func(x0+delta)):
        delta=delta
        find(delta,x0)
        break
    elif(func(x0-delta)<=func(x0)<=func(x0+delta)):
        delta=-delta
        find(delta,x0)
        break
    elif(func(x0-delta)<=func(x0)>=func(x0+delta)):
        print("re enter the values")
        continue
    else:
        print("the min is between {} and {}".format(x0-delta,x0+delta))
        break
