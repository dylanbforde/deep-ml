import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	grads = np.array(gradient)
	outputs = {}

	outputs['magnitude'] = np.linalg.norm(grads, 2)

	if outputs['magnitude'] != 0:
		outputs['direction'] = np.divide(grads, outputs['magnitude'])
		outputs['descent_direction'] = outputs['direction'] * -1
	else:
		outputs['direction'] = [0] * len(gradient)
		outputs['descent_direction'] = [0] * len(gradient)

	return outputs