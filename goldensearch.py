import math
print('This is Golden Section Search') 

def func(x):
    return 2*x+1.75*x**2+1.1*x**3+0.25*x**4
a=float(input("enter lower bound: ")) 
b=float(input("enter upper bound: "))
e=float(input("enter the termination parameter: "))
aw=0
bw=1
lw=bw-aw
k=1
while((lw*(b-a)>=e)):
    k=k+1 
    w1=aw+(0.618*lw)
    w2=bw-(0.618*lw)
    x1=((b-a)*w1)+a
    x2=((b-a)*w2)+a
    fw1=func(x1)
    fw2=func(x2)
    if(fw1>fw2):
        bw=w1
    if fw1<fw2:
        aw=w2
    lw=bw-aw
       
ll=((b-a)*aw)+a
ul=((b-a)*bw)+a
print("the interval is ",ll,"and",ul)
