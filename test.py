#-*-coding:utf8-*-
#!/usr/bin/env python
#unity test
import Roots


f1 = lambda x:x**2-4
f2 = lambda x:1-x**2
f3 = lambda x:x**3-3*x+2

def test_newton():
    """
    """
    assert Roots.solve_newton(f1,3) == 2,"Newton cannot calcualte f1"
    assert Roots.solve_newton(f2,1.5) == 1,"Newton cannot calculate f2"


def test_bisection():
    """

    """
    assert Roots.solve_bisection(f1,0,3) == 2,"Bisection cannot calculate f1"
    assert Roots.solve_bisection(f2,0,2) == 1,"Bisection cannot calculate f2"


def test_secant():
    """
    """
    # assert Roots.solve_secant(f1, 1, 3) == 2, "Secant method cannot calculate f1"
    # assert Roots.solve_secant(f2, 0.5, 2) == 1, "Secant method cannot calculate f2"
    print(Roots.solve_secant(f3,0,5))

if __name__ == '__main__':
    test_newton()
    test_bisection()
    test_secant()
    print("Test successed.")
