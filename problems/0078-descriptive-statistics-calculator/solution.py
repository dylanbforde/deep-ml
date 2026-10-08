import numpy as np
from collections import Counter

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    data = np.array(data)
    data = np.sort(data)
    n = len(data)

    midpoint = n // 2
    if n % 2 == 0:
        median = (data[midpoint - 1] + data[midpoint]) / 2
    else:
        median = data[midpoint]

    mean = np.sum(data) / n

    variance = (np.sum(data ** 2) / n) - (np.sum(data) / n) ** 2

    sd = np.sqrt(variance)

    num_counts = Counter(data)
    mode = num_counts.most_common()[0][0]

    
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "standard_deviation": sd,
        "25th_percentile": np.percentile(data, 25),
        "50th_percentile": np.percentile(data, 50),
        "75th_percentile": np.percentile(data, 75),
        "interquartile_range": np.percentile(data, 75) - np.percentile(data, 25)
        }
    
    