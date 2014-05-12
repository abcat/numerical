#-*-coding:utf8-*-
#!/usr/bin/env python
#This is the implements of methods to compute roots of equations.
from my_util import *


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
    The Newtons's methond for solving f(x)=0 draws the tangent to the graph of f(x)
    at any point and determines where the tangent intersects the x-axis.
    The method requires one starting value x.
    """
    x = float(x)
    for k in xrange(ns):
        (fx, Dfx) = (f(x), D(f)(x))
        (x_prev, x) = (x, x-fx/Dfx)
        if k>2 and abs(x - x_prev) < eps*abs(x):
            return x
    print("Error, no convergence.")


def solve_secant(f, a, b, eps=1e-6, ns=50):
    """
    """
    x0 = float(a)
    x1 = float(b)
    
    for k in xrange(ns):
        x = x1-((f(x1)*(x1-x0))/(f(x1)-f(x0)))
        x0 = x1
        x1 = x
        if abs(x1 - x0) < eps * abs(x1):
            return x
    print("Error, secant cannot converge the function")
