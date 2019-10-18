from params import*
from Harmonic import*
import matplotlib.pyplot as plt



t, theta = Harmonic.forced_damped()()


plt.plot(t, theta)
plt.show()