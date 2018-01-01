import numpy as np

cdef class Neuron:
    """ A biological model neuron introduced by
    Izhikevich (2003).
    """
    cdef double v, u, a, b, c, d

    def __init__(self, v, u, a, b, c, d):
        # State variables are v (observable membrane potential)
        # and u (hidden recovery variable)
        self.v = v
        self.u = u

        # These variables control dynamics in various ways
        self.a = a
        self.b = b
        self.c = c  # self.v is immediately reset to this value after AP
        self.d = d

    cpdef double dv(self, double I):
        """ Returns the time derivative of the membrane potential self.v
        """
        return 0.04*self.v*self.v + 5.0*self.v + 140.0 - self.u + I

    cpdef double du(self):
        """ Returns the time derivative of the recovery variable self.u
        """
        return self.a*(self.b*self.v - self.u)

    cpdef void evolve(self, double I, double dt):
        """ Updates state variables u and v, using the Euler method.
        """
        self.v += self.dv(I) * dt
        self.u += self.du() * dt
        if self.v >= 30.0:
            self.v = self.c
            self.u += self.d


def simulate(Neuron neuron, double[:] I, double dt):
    """ Takes a neuron, a 1-dimensional memoryview I representing
    a time series of current input to the neuron, and a time step dt
    between consecutive values of I. Returns a record of the membrane
    potential of the neuron as a numpy array with the same length as I.
    """
    cdef unsigned int i, n = I.shape[0]
    record = np.zeros(n)
    for i in range(n):
        record[i] = neuron.v
        neuron.evolve(I[i], dt)
    return record


def example():
    neuron = Neuron(-65.0, 0.0, 0.02, 0.2, -65.0, 2.0)
    return simulate(neuron, 0.0001, 1000000)

