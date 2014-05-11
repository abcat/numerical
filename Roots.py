#-*-coding:utf8-*-
#!/usr/bin/env python
#This is the implements of methods to compute roots of equations.
from my_util impport *


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


def solve_bisection(f, a, b, eps=1e-6, ns=100):
    """
    input:  -f function to solve
            -a,b interval
    """
    #make sure a and is in different signs
    fa = f(a)
    if fa == 0:
        return a
    fb = f(b)
    if fb == 0:
        return b

    if fa*fb > 0:
        print("Error, a and b should in different sign")
        return "error"

    #main loop
    for k in xrange(ns):
        x = (a+b)/2
        fx = f(x)
        if f(x) == 0 or abs(b-a)<eps:
            return x
        elif sign(fx) == sign(fa):
            (a,fa) = (x,fx)
        elif sign(fx) == sign(fa):
            (b,fb) = (x,fx)
    print("Error, no convergence.")


def solve_newton(f, x, eps=1e-6, ns=20):
    """

    """
    x = float(x)
    for k in xrange(ns):
        (fx, Dfx) = (f(x), D(f)(x))
        (x_prev, x) = (x, x-fx/Dfx)
        if k>2 and abs(x - x_prev) < eps*abs(x):
            return x
    print("Error, no convergence.")

