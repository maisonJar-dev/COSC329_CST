import numpy as np
from numpy import linalg as LA

def cosine_matrix(X: np.ndarray) -> np.ndarray:
    norms = LA.norm(X, axis=1,keepdims=True)
    norms[norms == 0] = 1
    return X @ X.T / (norms @ norms.T)