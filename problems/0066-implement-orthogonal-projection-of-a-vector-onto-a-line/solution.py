import numpy as np

def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	v = np.array(v)
	L = np.array(L)

	num = np.dot(v, L)
	den = np.dot(L, L)

	frac = np.divide(
		num,
		den,
		where=np.abs(den) > 1e-10
	)

	return np.dot(frac, L)