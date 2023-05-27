import numpy as np

def scale(arr):
    val = np.max(arr)
    scaled_arr = arr / val
    sum = np.sum(scaled_arr)
    rou = round(sum, 4)
    return rou