from sympy.solvers import solve
from sympy import Symbol
from sympy import sqrt
import numpy as np

def f(x1, x2):
	return x1**3 + 5 + x2**2 - 4*x2 + 4

def gradient(x1, x2):
	gradf = [3*x1**2, 2*x2 - 4]
	return gradf

def modgrad(gradf):
	return sqrt(gradf[0]**2 + gradf[1]**2)

def deriv(gradf, x_old, lambd):
	lambd = Symbol('l', real=True)
	return (-3)*gradf[0]*(x_old[0] - lambd*gradf[0])**2 - 2*gradf[1]*(x_old[1] - lambd*gradf[1]) + 4*gradf[1]

eps = float(input("Eps: "))
x_old = np.array([0.5, 1]) #pochatkove nablyzhennia
mod= 1000
lambd_arr = []
while mod > eps:
	grad = np.array(gradient(x_old[0], x_old[1]))
	mod = modgrad(grad)
	l = Symbol('l', real=True)
	e = deriv(grad, x_old, l)
	lamd = solve(e, l)
	for i in range(len(lamd)):
		lambd_arr.append(lamd[i])
	lambd = min(lambd_arr)
	x_new = x_old - lambd*grad
	x_old = x_new

print("X optimal = " + str(x_new))
print("F optimal = " + str(f(x_new[0], x_new[1])))
