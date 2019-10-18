from params import*
from dampedharmonic import*
import matplotlib.pyplot as plt
t, theta = rk4()
plt.plot(t, theta)
plt.show()