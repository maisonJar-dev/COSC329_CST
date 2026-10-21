import numpy as np
from numpy import linalg as LA

def cosine_matrix(X: np.ndarray) -> np.ndarray:
    norms = LA.norm(X, axis=1,keepdims=True)
    return X @ X.T / (norms @ norms.T)