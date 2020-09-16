import numpy as np
import matplotlib.pyplot as plt


# Dimensionless parameters
a = 0.0008

font={'size': 22}

f = np.linspace(0, 5, 100)
x = 0.5 * (1 - (f + a) + np.sqrt((f + a - 1)**2 + 4 * a * (1 + f)))
eps = (1 - 2 * x) - ((2 * f * x * a)/(a + x)**2)

plt.plot(f, eps, 'k', linewidth=2)
plt.text(0.7, 0.2, 'Limit Cycle Region', size=30)
plt.text(0.6, 0.05, 'Unstable equilibrium points', size=26)
plt.text(1.3, 0.8, 'Stable equilibrium points', size=26)
plt.fill_between(f, -1.5, eps, color='salmon')
plt.xlabel("f", fontdict=font)
plt.ylabel("\u03B5(f)", fontdict=font)
plt.xticks(size = 22)
plt.yticks(size = 22)
plt.tight_layout()
plt.savefig('epsfplotOregonator.pdf', bbox_inches='tight')
plt.show()

