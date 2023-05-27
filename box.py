import numpy as np

def box(f):
    a = (4/3) * np.pi * (f**3)
    b = np.sum(a)
    c = round(b, 4)
    return c