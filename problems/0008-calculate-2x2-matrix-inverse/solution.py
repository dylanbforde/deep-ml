import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """

    matrix = np.array(matrix)
    det = np.linalg.det(matrix)
    
    if det == 0:
        return None
    M_sqz = matrix.ravel()
    
    M_arr = [
        M_sqz[3], -1 * M_sqz[1], -1 * M_sqz[2], M_sqz[0]
        ]

    M_arr = np.array(M_arr).reshape(-1, 2)
    A_inv = (1 / det) * M_arr

    return A_inv
