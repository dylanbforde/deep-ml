import numpy as np

def calculate_correlation_matrix(X, Y=None):
	X = np.array(X)
	
	if Y is None:
		Y = X
	else:
		Y = np.array(Y)

	n_samples = X.shape[0]
	dof = n_samples - 1
	if Y.shape[0] != n_samples:
		raise ValueError("require same number of samples")

	Xc = X - X.mean(axis=0, keepdims=True)
	Yc = Y - Y.mean(axis=0, keepdims=True)
	
	cov_xx = Xc.T @ Xc / dof
	cov_xy = Xc.T @ Yc / dof
	cov_yy = Yc.T @ Yc / dof
	
	std_x = np.sqrt(cov_xx.diagonal())
	std_y = np.sqrt(cov_yy.diagonal())

	corr = cov_xy / np.outer(std_x, std_y)
	return corr.tolist()