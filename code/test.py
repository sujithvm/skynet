import numpy as np
from pso import pso

###############################################################################

def banana(x):
    x1 = x[0]
    x2 = x[1]
    return x2 - x1

lb = [-3, -1]
ub = [2, 6]

xopt, fopt = pso(banana, lb, ub)


print xopt

print banana([xopt[0], xopt[1]])

print fopt

