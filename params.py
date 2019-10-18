import numpy as np

#Params
l = 1.0 #length of pendulum
g = 9.81 #gravittional acceleration
theta0 = 0.2 #initial angle in radians
omega0 = 0.0 #Initial angular velocity in radians
q = 1.0 #damping parameter
F_D = 0.2 #Driving force
Omega_D = np.sqrt(g/l)


#Forces
def driving_force(t):
    return F_D*np.sin(Omega_D*t)