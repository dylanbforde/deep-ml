def poly_term_derivative(c: float, x: float, n: float) -> float:
    coeff = c * n
    n_after = n - 1
    return coeff * x ** n_after