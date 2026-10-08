from collections import Counter

def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """

    counts = Counter(samples)
    
    dct = {}
    for key, value in counts.items():
        dct[key] = value / len(samples)

    return [(key, value) for key, value in dct.items()]
