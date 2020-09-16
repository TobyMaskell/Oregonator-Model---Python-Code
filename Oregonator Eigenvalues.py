import numpy as np
from numpy.linalg import eig

# Parameters
a = 0.0008
f = 2.34
eps = 0.04

# Equilibrium point
x = 0.5 * (1 - (f + a) + np.sqrt((f + a - 1)**2 + 4 * a * (1 + f)))

# Jacobian matrix
J = np.array([[(1 - 2 * x - (2 * f * x * a / (x + a)**2)) / eps, (f * (a - x)/(a + x)) / eps], [1, -1]])

# Eigenvalues
eigvals, eigvecs = eig(J)

print(eigvals)