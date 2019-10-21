import params
import numpy as np


class Harmonic:
    """
    Each class method returns a function.
    Writing Harmonic.damped(q)( ) returns the solution of a damped
    harmonic oscillator for a given friction coefficient q.
    Writing Harmonic.forced_damped()() returns the solution of a damped
    harmonic oscillator for the external force and friction coefficient q defined
    in params.py
    """
    def __init__(self, friction=1, force=None):
        self.friction = friction
        self.force = force

    @classmethod
    def damped(cls, friction):
        return cls(friction)

    @classmethod
    def forced_damped(cls, force = params.driving_force, friction=params.q):
        return cls(friction, force)

    def __call__(self, step=0.01, stop=10, start=0):
        def omega_prime(theta, omega, t):
            """
            :return: derivative of omega with respect to time at some point theta
            """
            if self.force is not None:
                external_force = self.force(t)
            else:
                external_force = 0
            return -(params.g / params.l) * theta - self.friction * omega + external_force

        def theta_prime(omega):
            """
            :return: derivative of theta with respect to time at some point omega
            """
            return omega

        t = np.arange(start, stop, step)
        n = int((stop - start) / step)
        omega = np.zeros(n)
        theta = np.zeros(n)
        omega[0], theta[0] = params.omega0, params.theta0
        for i in range(n - 1):
            # calculate next omega
            o1 = omega_prime(theta[i], omega[i], t[i])
            o2 = omega_prime(theta[i] + o1 * step / 2, omega[i], t[i])
            o3 = omega_prime(theta[i] + o2 * step / 2, omega[i], t[i])
            o4 = omega_prime(theta[i] + o3 * step, omega[i], t[i])
            omega[i + 1] = omega[i] + (step / 6) * (o1 + 2 * o2 + 2 * o3 + o4)

            # calculate next theta
            t1 = theta_prime(omega[i])
            t2 = theta_prime(omega[i] + t1 * step / 2)
            t3 = theta_prime(omega[i] + t2 * step / 2)
            t4 = theta_prime(omega[i] + t3 * step)
            theta[i + 1] = theta[i] + (step / 6) * (t1 + 2 * t2 + 2 * t3 + t4)

        work = 0.5*(params.l**2) * (omega*omega - params.omega0**2) + (params.g*params.l)*(theta*theta - params.theta0**2)
        return t, theta, work

