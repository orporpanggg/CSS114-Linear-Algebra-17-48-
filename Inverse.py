import numpy as np

def inverse_method(A, b):
    A_inv = np.linalg.inv(A)   # ใช้สูตร inverse
    x = A_inv.dot(b)
    return A_inv, x