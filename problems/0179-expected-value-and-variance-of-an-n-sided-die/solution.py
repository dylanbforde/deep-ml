import numpy as np

def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	values = [num for num in range(1, n+1)]
	values = np.array(values)

	expected_value = np.sum(values) / n
	variance = (np.sum(values ** 2) / n) - (expected_value ** 2)

	return (expected_value, variance)
