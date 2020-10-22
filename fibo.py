import math
print('This is Fibonacci Search') 

def func(x):
    return math.sin(x)+4*x*x
def fib(n):
    k1=1;
    k2=1;
    while(n-1):
        fibo.append(k1+k2)
        k2=k1+k2
        k1=k2-k1
        n-=1
fibo=[]
fibo.append(0)
fibo.append(1)
 
a=float(input("enter a"))
b=float(input("enter b"))
m=int(input(" enter number of function evaluations"))
fib(m+1)
k=2
l=(b-a)
while(k<=m):
    lk=(fibo[m-k+1]/(float)(fibo[m+1]))*l
    x1=a+lk
    x2=b-lk
    if(func(x1)>func(x2)):
        a=x1
    elif(func(x1)<func(x2)):
        b=x2
    k+=1
    
print("the minimum lies between {} and {}".format(a,b))
