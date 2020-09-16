import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import matplotlib.patches as patches

font={'size': 14}

# Dimensionless parameters
eps = 0.04
a = 0.0008
f = 3

# Oregonator model
def Oregonator(t, Y):
    x,z = Y;
    return [(x * (1 - x) + ((a - x) * f * z) / (a + x)) / eps, x - z]

# Time span, inital conditions
ts = np.linspace(0, 10, 2000)
Y0 = [1, 0.5]


# Numerical algorithm/method
NumSol = solve_ivp(Oregonator, [0, 30], Y0, method="Radau")
t = NumSol.t
x,z = NumSol.y


# Plot of results for x and z
plt.subplot(221);
plt.plot(t,x,'b'); plt.xlabel("\u03C4", fontdict=font); plt.ylabel("x(\u03C4)", fontdict=font);
plt.xticks(size = 12)
plt.yticks(size = 12)
plt.subplot(222);
plt.plot(t,z,'r'); plt.xlabel("\u03C4", fontdict=font); plt.ylabel("z(\u03C4)", fontdict=font);

# Circles for Phase Portrait
# circ = patches.Circle((1, 0.5), radius=0.005, linewidth=5, edgecolor='k', facecolor='k')
# plt.gca().add_patch(circ)

#Phase portrait

#plt.subplot(223);
#plt.plot(x,z,'g'); plt.xlabel("x", fontdict=font); plt.ylabel("z", fontdict=font);


plt.xticks(size = 12)
plt.yticks(size = 12)
plt.tight_layout();
plt.savefig('OregNSf=3.pdf', bbox_inches='tight')
#plt.show()


