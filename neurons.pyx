
def izhikevich(double v, double u, double I):
    cdef:
        double a = 0.02 
        double b = 0.2
        double dv = 0.04*v*v + 5*v + 140 - u + I
        double du = a * (b*v - u)
    return dv, du


def simulate(int n, double dt, double I):
    cdef:
        double v = -65 
        double u = 0
        double c = -65
        double d = 2
        list record = [None] * n
    for i in range(n):
        dv, du = izhikevich(v, u, I)
        v += dt * dv
        u += dt * du
        if v >= 30:
            v = c
            u += d
        record[i] = v
    return record
    
