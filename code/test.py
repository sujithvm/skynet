import numpy as np
from pso import pso

###############################################################################

def banana(x):
    x1 = x[0]
    x2 = x[1]
    return x1 - x2


lb = [0, 10]
ub = [10, 100]

xopt, fopt = pso(banana, lb, ub)

print xopt

print banana([xopt[0], xopt[1]])

print fopt

