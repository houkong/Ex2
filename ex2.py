from params import*
from Harmonic import*
import matplotlib.pyplot as plt
import numpy as np
import os

t1, theta1, w1 = Harmonic.damped(1)()
t2, theta2, w2 = Harmonic.damped(2)()
t3, theta3, w3 = Harmonic.damped(6)()

plt.plot(t1, theta1, label="q = 1, underdamped")
plt.plot(t2, theta2, label="q = 2, critical damping")
plt.plot(t3, theta3, label="q = 6, overdamped")
plt.xlabel("t [s]")
plt.ylabel("θ [rad]")
plt.title("Damped harmonic oscillator")
plt.legend()
if not os.path.exists("plots"):
    os.mkdir("plots")
plt.savefig("plots/damped_harmonic.png")
plt.show()


plt.plot(t1, w1, label="q = 1, underdamped")
plt.plot(t2, w2, label="q = 2, critical damping")
plt.plot(t3, w3, label="q = 6, overdamped")
plt.xlabel("t [s]")
plt.ylabel("W [J/kg]")
plt.title("Work done by damped harmonic oscillator")
plt.legend()
if not os.path.exists("plots"):
    os.mkdir("plots")
plt.savefig("plots/damped_harmonic_work.png")
plt.show()


t1, theta1, _ = Harmonic.forced_damped(force=lambda t : F_D*np.sin(0.7*Omega_D*t))(stop=20)
t2, theta2, _ = Harmonic.forced_damped(force=lambda t : F_D*np.sin(0.8*Omega_D*t))(stop=20)
t3, theta3, _ = Harmonic.forced_damped(force=lambda t : F_D*np.sin(Omega_D*t))(stop=20)




plt.plot(t1, theta1, label="0.5Ω")
plt.plot(t2, theta2, label="0.8Ω")
plt.plot(t3, theta3, label="1.0Ω")
plt.xlabel("t [s]")
plt.ylabel("θ [rad]")
plt.title("Damped harmonic oscillator with external driving force")
plt.legend()
if not os.path.exists("plots"):
    os.mkdir("plots")
plt.savefig("plots/forced_harmonic.png")
plt.show()