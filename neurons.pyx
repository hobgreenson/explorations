
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
        self.c = c
        self.d = d

    def evolve(self, double dt):
        """ Updates state variables u and v, using Euler method.
        """
        cdef: 
            double dv = 0.04*self.v*self.v + 5*self.v + 140 - self.u + self.I
            double du = self.a*(self.b*self.v - self.u)
        self.v += dv*dt
        self.u += du*dt
        if self.v >= 30:
            # Reset at peak of action potential
            self.v = self.c
            self.u += self.d


def simulate(Neuron neuron, double dt, long n):
    cdef list record = [None] * n
    for i in range(n):
        record[i] = neuron.v
        neuron.evolve(dt)
    return record


def example():
    neuron = Neuron(-65, 0, 50, 0.02, 0.2, -65, 2)
    return simulate(neuron, 0.0001, 1000000)

