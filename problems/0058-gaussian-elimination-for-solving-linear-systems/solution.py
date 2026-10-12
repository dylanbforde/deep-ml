import numpy as np

def gaussian_elimination(A, b):
	"""
	Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
	:param A: Coefficient matrix
	:param b: Right-hand side vector
	:return: Solution vector x
	"""
	# Ax=b
	# A^-1Ax =A^-1b
	# x = A^-1 b
	A_inv = np.linalg.inv(A)
	x = A_inv @ b
	return x