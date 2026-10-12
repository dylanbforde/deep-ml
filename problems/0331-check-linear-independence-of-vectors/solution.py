import numpy as np

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    """
    Check if a set of vectors is linearly independent.
    
    Args:
        vectors: List of vectors, where each vector is a list of floats.
                 All vectors must have the same dimension.
        
    Returns:
        True if vectors are linearly independent, False otherwise.
    """
    if len(vectors) == 0:
        return True

    M = np.array(vectors)
    _, s, _ = np.linalg.svd(M)

    if np.count_nonzero(s > 1e-8) == len(vectors):
        return True
    else:
        return False