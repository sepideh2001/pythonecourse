import math 
def sin(x,n):
    sine=0 
    for i in range(n): 
        sign=math.pow(-1,i)
        pi=math.pi 
        a=x*(pi/180)
        sine=sine+(sign*(a**(2.0*i+1))/math.factorial(2*i+1))
    return sine 
    
x=float(input('enter the value of degrees:'))
n=int(input('enter the number of terms:'))
print(sin(x,n))