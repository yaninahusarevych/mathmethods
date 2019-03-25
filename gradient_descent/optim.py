import matplotlib.pyplot as plt
import autograd.numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LogNorm
from autograd import elementwise_grad, value_and_grad
from sympy.solvers import solve
from sympy import Symbol
from sympy import sqrt
import numpy as np

f  = lambda x1, x2: ((x1 + 1)**2)/100 + ((x2 + 2)**4)/200

def gradient(x1, x2):
	gradf = [(2/100)*(x1 + 1), (4/200)*(x2 + 2)**3]
	return gradf

def modgrad(gradf):
	return sqrt(gradf[0]**2 + gradf[1]**2)

def deriv(gradf, x_old, lambd):
	lambd = Symbol('l', real=True)
	return (-2/100)*gradf[0]*(x_old[0] - lambd*gradf[0] + 1)**3 - (4/200)*gradf[1]*(x_old[1] - lambd*gradf[1] + 2)**3

eps = float(input("Eps: "))
mod = 1000
it = 0
while True:
	if it == 0:
		x_old = np.array([0.5, 1]) #pochatkove nablyzhennia
	grad = np.array(gradient(x_old[0], x_old[1]))
	mod = modgrad(grad)
	if mod < eps:
		break
	l = Symbol('l', real=True)
	e = deriv(grad, x_old, l)
	lamd = solve(e, l)
	x_new = x_old - lamd*grad
	x_old = x_new
	it+=1

xmin, xmax, xstep = -10, 10, .1
ymin, ymax, ystep = -10, 10, .1
x1, x2 = np.meshgrid(np.arange(xmin, xmax + xstep, xstep), np.arange(ymin, ymax + ystep, ystep))
z = f(x1, x2)
minima = np.array([x_new[0], x_new[1]])
minima_ = minima.reshape(-1, 1)
fig = plt.figure(figsize=(8, 5))
ax = plt.axes(projection='3d', elev=50, azim=-50)
ax.plot_surface(x1, x2, z, norm=LogNorm(), rstride=1, cstride=1, 
                edgecolor='none', alpha=.8, cmap=plt.cm.jet)
ax.plot(*minima_, f(*minima_), 'r*', markersize=10)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')
ax.set_xlim((xmin, xmax))
ax.set_ylim((ymin, ymax))
plt.show()
dz_dx1 = elementwise_grad(f, argnum=0)(x1, x2)
dz_dx2 = elementwise_grad(f, argnum=1)(x1, x2)
fig, ax = plt.subplots(figsize=(10, 6))
ax.contour(x1, x2, z, levels=np.logspace(0, 5, 35), norm=LogNorm(), cmap=plt.cm.jet)
ax.quiver(x1, x2, x1 - dz_dx1, x2 - dz_dx2, alpha=.5)
ax.plot(*minima_, 'r*', markersize=18)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim((xmin, xmax))
ax.set_ylim((ymin, ymax))
plt.show()
print("X optimal = " + str(x_new))
print("F optimal = " + str(f(x_new[0], x_new[1])))
print("Iterations = " + str(it))