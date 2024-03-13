import sympy as sym
import numpy as np


def grad(f, var, A):
    a = []
    podst = list(zip(var, A))
    for x in var:
        a.append(sym.diff(f, x, 1).subs(podst))
    return np.array(a)


def grad_fall(f, var, A, k):
    gf = grad(f, var, A)
    A = np.array(A)
    A = A - k * gf
    return A


x = sym.Symbol('x')
y = sym.Symbol('y')
f = 13*x**3-7*x*y+y**2+2*y**3-97
A = (1, 2)
k = 0.1
A1 = grad_fall(f, (x, y), A=A, k=k)
gf = grad(f, (x, y), A1)
A2 = grad_fall(f, (x, y), A=A1, k=k)
print(A2)
print()