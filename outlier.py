import numpy as np

def outlier(f):
    a = np.mean(f)
    b = np.std(f)
    cnt = np.abs(f - a) > b
    return cnt