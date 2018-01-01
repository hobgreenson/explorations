from libc cimport math

cdef class Neuron:
    """ A biological model neuron introduced by
    Izhikevich (2003).
    """
    cdef double v, u, I, a, b, c, d
    def __init__(self, v, u, I, a, b, c, d):
        # State variables are v (observable membrane potential)
        # and u (hidden recovery variable)
        self.v = v
        self.u = u

        # The current I is the net input to the neuron
        self.I = I

        # These variables control dynamics in various ways
        self.a = a
        self.b = b
        self.c = c  # self.v is immediately reset to this value after AP
        self.d = d
    
    cpdef double dv(self):
        """ Returns the time derivative of the membrane potential self.v
        """
        return 0.04*self.v*self.v + 5.0*self.v + 140.0 - self.u + self.I

    cpdef double du(self):
        """ Returns the time derivative of the recovery variable self.u
        """
        return self.a*(self.b*self.v - self.u)

    cpdef void evolve(self, double dt):
        """ Updates state variables u and v, using the Euler method.
        """
        self.v += self.dv() * dt
        self.u += self.du() * dt
        if self.v >= 30:
            self.v = self.c
            self.u += self.d


def simulate(Neuron neuron, double dt, unsigned int n):
    cdef list record = [None] * n
    for i in range(n):
        record[i] = neuron.v
        neuron.evolve(dt)
    return record


def example():
    neuron = Neuron(-65, 0, 50, 0.02, 0.2, -65, 2)
    return simulate(neuron, 0.0001, 1000000)

