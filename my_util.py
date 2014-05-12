#-*-coding:utf8-*-
#!/usr/bin/env python
#implement some useful functions


def D(f, h = 1e-6):
    """
    first derivative of f
    get the algorithm from the define of derivative
    """
    return lambda x,f=f,h=h: (f(x+h)-f(x-h))/2/h


def DD(f, h = 1e-6):
    """
    second derivative of f
    """
    return lambda x,f=f,h=h: (f(x+h)-2.0*f(x)+f(x-h))/(h*h)



def sign(x):
    """
    calculate the sing of x
    if x>0, return 1
    if x=0, return 0
    if x<0, return -1
    """
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1
