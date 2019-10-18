import numpy as np
import params


def rk4(step=0.1, stop=10, start=0):
    q = 1
    def omega_prime(theta, omega):
        """
        :return: derivative of omega with respect to time at some point theta
        """
        return -(params.g / params.l) * theta - q*omega

    def theta_prime(omega):
        """
        :return: derivative of theta with respect to time at some point omega
        """
        return omega
    t = np.arange(start, stop, step)
    n = int((stop - start)/step)
    omega = np.zeros(n)
    theta = np.zeros(n)
    omega[0], theta[0] = params.omega0, params.theta0
    for i in range(n-1):
        # calculate next omega
        o1 = omega_prime(theta[i], omega[i])
        o2 = omega_prime(theta[i] + o1 * step / 2, omega[i])
        o3 = omega_prime(theta[i] + o2 * step / 2, omega[i])
        o4 = omega_prime(theta[i] + o3 * step, omega[i])
        omega[i + 1] = omega[i] + (step/6)*(o1 + 2*o2 + 2*o3 + o4)

        # calculate next theta
        t1 = theta_prime(omega[i])
        t2 = theta_prime(omega[i] + t1 * step / 2)
        t3 = theta_prime(omega[i] + t2 * step / 2)
        t4 = theta_prime(omega[i] + t3 * step)
        theta[i + 1] = theta[i] + (step/6)*(t1 + 2 * t2 + 2 * t3 + t4)

    return t, theta