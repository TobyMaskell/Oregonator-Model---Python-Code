import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import solve_ivp


fig = plt.figure(figsize=(4,3))
ax = fig.gca(projection='3d')

# Dimensionless parameters
eps = 0.04
q = 0.0008


f=1.
# Oregonator model
def Oregonator(t, Y):
    x,z = Y;
    return [(x * (1 - x) + ((q - x) * f * z) / (q + x)) / eps, x - z]
# Time span, inital conditions
ts = np.linspace(0, 10, 100)


Y0 = [0.5, 0.3]
# Numerical algorithm/method
NumSol = solve_ivp(Oregonator, [0, 30], Y0, method="Radau")
t = NumSol.t
x,z = NumSol.y
# Plot of results for x and z
# Phase portrait
#plt.subplot(211);
#plt.plot(x,z); plt.xlabel("x"); plt.ylabel("z"); plt.tight_layout();
x1=x
z1=z


f=1.5
Y0 = [0.5, 0.3]
NumSol = solve_ivp(Oregonator, [0, 30], Y0, method="Radau")
t = NumSol.t
x,z = NumSol.y
x2=x
z2=z

f=2
Y0 = [0.5, 0.3]
NumSol = solve_ivp(Oregonator, [0, 30], Y0, method="Radau")
t = NumSol.t
x,z = NumSol.y
x3=x
z3=z

f=0.6
Y0 = [0.5, 0.3]
NumSol = solve_ivp(Oregonator, [0, 40], Y0, method="Radau")
t = NumSol.t
x,z = NumSol.y
x4=x
z4=z



f=2.2
Y0 = [0.5, 0.3]
NumSol = solve_ivp(Oregonator, [0, 40], Y0, method="Radau")
t = NumSol.t
x,z = NumSol.y
x5=x
z5=z

f=0.51
Y0 = [0.5, 0.3]
NumSol = solve_ivp(Oregonator, [0, 40], Y0, method="Radau")
t = NumSol.t
x,z = NumSol.y
x6=x
z6=z
plt.subplot(211);
plt.plot(t,x); plt.xlabel("t"); plt.ylabel("x"); plt.tight_layout();
plt.subplot(212);
plt.plot(x,z); plt.xlabel("x"); plt.ylabel("z"); plt.tight_layout();
#plt.plot(x,z); plt.xlabel("x"); plt.ylabel("z"); plt.tight_layout();
# Plot of results for x and z


#plt.plot(x,z,x1,z1); plt.xlabel("x"); plt.ylabel("z"); plt.tight_layout();

plt.show()
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(1.5*np.ones(len(x2)), x2, z2)
ax.plot(1.*np.ones(len(x1)), x1, z1)
ax.plot(2.*np.ones(len(x3)), x3, z3)
ax.plot(0.6*np.ones(len(x4)), x4, z4)
ax.plot(2.2*np.ones(len(x5)), x5, z5)
ax.plot(0.51*np.ones(len(x6)), x6, z6)
ax.set_xlabel('$f$', fontsize=20)
ax.set_ylabel('$x$', fontsize=20)
ax.set_zlabel('$z$', fontsize=20)


a = 0.0008
f = np.linspace(0, 0.5, 500)

def x(f):
    return 0.5 * (1 - (f + a) + np.sqrt((f + a - 1)**2 + 4 * a * (1 + f)))

def z(f):
    return 0.5 * (1 - (f + a) + np.sqrt((f + a - 1) ** 2 + 4 * a * (1 + f)))

ax.plot(f, x(f), z(f), 'm')

f = np.linspace(2.5, 5, 500)

def x(f):
    return 0.5 * (1 - (f + a) + np.sqrt((f + a - 1)**2 + 4 * a * (1 + f)))

def z(f):
    return 0.5 * (1 - (f + a) + np.sqrt((f + a - 1) ** 2 + 4 * a * (1 + f)))

ax.plot(f, x(f), z(f), 'm')

plt.xticks(size = 16)
plt.yticks(size = 16)

plt.grid()
plt.savefig('BifurcationPlotFINAL.pdf', bbox_inches='tight')
plt.show()