import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

font={'size': 26}

# Dimensionless parameters
eps = 0.04
a = 0.0008
f = 1

# Oregonator model nullcline curves as numpy array
def Oregnull(Y, t = 0):
    return np.array((Y[0] * (1 - Y[0] - ((Y[0] - a) * f * Y[1]) / (Y[0] + a)) / eps, Y[0] - Y[1] ))

# x = np.linspace(0, 5, 30)


# Domain of variables
x1 = np.linspace(0, 0.8, 1000)
x2 = [0, 0.08]
z = np.linspace(0, 0.8, 1000)


# Deal with asymptotic behaviour!

# Oregonator model nullcline curves
split = a + 0.00001
x_small = np.linspace(a + 0.000001, split, 2000)
x_big = np.linspace(split, 1, 1000)
x1 = np.array([*x_small, *x_big])
x2 = np.array([0, 1])
v = x2

u = ((1 - x1)*(a + x1)*x1 /(f*(x1-a))) #/ eps
#u[u<q] = np.nan
#u[u> 7] = np.nan

# Plot nullclines
plt.plot(x1, u, 'r-', lw=2, label='x-nullcline', zorder = 0)
plt.plot(x2, v, 'b-', lw=2, label='z-nullcline')


# Add quadrilateral and plot
rect = patches.Rectangle((0, 0.009), 0.8, 0.35, linewidth=2, edgecolor='k', facecolor='none')
plt.gca().add_patch(rect)

# Equilibrium point and plot
circ = patches.Circle((0.04, 0.04), radius=0.015, linewidth=2, edgecolor='k', facecolor='none')
plt.gca().add_patch(circ)

# Individual Quivers with plots on rectangle
x1_pos = 0.4
z1_pos = 0.009
x2_pos = 0.8
z2_pos = 0.2
z3_pos = 0.36
x3_pos = 0
x1_direct = 1
z1_direct = 0
x2_direct = 0
z2_direct = 1
x3_direct = -1
z3_direct = 0
z4_direct = -1


plt.quiver(x1_pos,z1_pos,x1_direct,z1_direct, scale=30)
plt.quiver(x2_pos,z2_pos,x2_direct,z2_direct, scale=30)
plt.quiver(x1_pos,z3_pos,x3_direct,z3_direct, scale=30)
plt.quiver(x3_pos,z2_pos,x2_direct,z4_direct, scale=30)

# Repelling region

xss1_pos = 0.05
zss1_pos = 0.1
xss2_pos = 0.06
zss2_pos = 0.03
xss3_pos = 0.03
zss3_pos = 0.07
xss_direct = 1
xss2_direct = -0.2
xss3_direct = 1.9
zss1_direct = 1.7
zss2_direct = 0.3

#plt.quiver(xss1_pos,zss1_pos,xss3_direct,zss1_direct, scale=65)
plt.quiver(xss2_pos,zss2_pos,xss_direct,zss2_direct, scale=55)
plt.quiver(xss3_pos,zss3_pos,xss2_direct,z2_direct, scale=55)

# Concentration annotations
plt.text(0.03, 0.3, 'High [$Br^-$]', fontsize=18)
plt.text(0.65, 0.05, 'Low [$Br^-$]', fontsize=18)
plt.text(0.45, 0.3, 'High [$HBrO_2$]', fontsize=18)
plt.text(0.45, 0.05, 'Low [$HBrO_2$]', fontsize=18)
plt.text(0.65, 0.3, 'High [$M_{ox}$]', fontsize=18)
plt.text(0.15, 0.05, 'Low [$M_{ox}$]', fontsize=18)

# Plot
plt.xlabel("x", fontdict=font)
plt.ylabel("z", fontdict=font)
plt.xticks(size = 22)
plt.yticks(size = 22)
plt.legend(loc='upper center', prop={'size': 24})
plt.grid()
plt.show()








# Add quivers/arrows
#X1 , Z1  = np.meshgrid(x1, z)                 # Create a grid
#DX1, DZ1 = Oregnull([X1, Z1])                 # Adjacent and opposite sides of triangle for quivers/arrows
#M = (np.hypot(DX1, DZ1))                      # Hypotenuse of triangle for quivers/arrows
#M[ M == 0] = 1.                               # Avoid zero division errors
#DX1 /= M                                      # Normalise the arrows
#DZ1 /= M
#plt.quiver(X1, Z1, DX1, DZ1, M, pivot='mid', scale=90)  # Plot


# Initial lists containing values
# x = []
# z = []

# def sys(iv1, iv2, dt, time):
    # initial values:
  #  x.append(iv1)
   # z.append(iv2)
    # Compute and fill lists
  #  for i in range(time):
  #      x.append(x[i] + (g(x[i])) * dt)
  #      z.append(z[i] + (h(x[i])) * dt)
   # return x, z

# sys(1, 0.5, 0.01, 30)

# Locate and find equilibrium points
# eqp = []

# def find_fixed_points(r):
#    for x in range(r):
#        for z in range(r):
#            if ((g(x, z) == 0) and (h(x, z) == 0)):
#                eqp.append((x,z))

#    return eqp

# Plot equilibrium points
# for point in eqp:
#   plt.plot(point[0],point[1],"red", marker = "o", markersize = 10.0)