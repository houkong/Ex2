from params import*
from Harmonic import*
import matplotlib.pyplot as plt
import os

t1, theta1 = Harmonic.damped(2)()
t2, theta2 = Harmonic.damped(5)()
t3, theta3 = Harmonic.damped(10)()

plt.plot(t1, theta1, label="q = 2, underdamped")
plt.plot(t2, theta2, label="q = 5, critical damping")
plt.plot(t3, theta3, label="q = 10, overdamped")
plt.xlabel("t [s]")
plt.ylabel("θ [rad]")
plt.title("Damped harmonic oscillator")
plt.legend()
if not os.path.exists("plots"):
    os.mkdir("plots")
plt.savefig("plots/damped_harmonic.png")