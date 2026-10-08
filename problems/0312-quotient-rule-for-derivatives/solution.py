import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """

    g_coeffs = np.array(g_coeffs, dtype=float)
    h_coeffs = np.array(h_coeffs, dtype=float)

    g_x = np.polyval(g_coeffs, x)
    h_x = np.polyval(h_coeffs, x)

    g_prime_coeffs = np.polyder(g_coeffs)
    h_prime_coeffs = np.polyder(h_coeffs)

    g_prime_x = np.polyval(g_prime_coeffs, x)
    h_prime_x = np.polyval(h_prime_coeffs, x)

    derivative = (g_prime_x * h_x - g_x * h_prime_x) / (h_x ** 2)
    return float(derivative)
