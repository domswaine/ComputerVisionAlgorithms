import numpy as np


def sum_of_absolute_differences(a, b):
    return np.sum(np.abs(a - b))


def cross_correlation(a, b):
    return np.sum(a * b)


def normalised_cross_correlation(a, b):
    numerator = cross_correlation(a, b)
    denominator = np.sqrt(np.sum(a * a)) * np.sqrt(np.sum(b * b))
    return numerator / denominator


def cosine(a, b):
    return normalised_cross_correlation(a, b)


def correlation_coefficient(a, b):
    normalised_a = a - np.mean(a)
    normalised_b = b - np.mean(b)
    numerator = cross_correlation(normalised_a, normalised_b)
    denominator = np.sqrt(np.sum(np.square(normalised_a))) * np.sqrt(np.sum(np.square(normalised_b)))
    return numerator / denominator


def euclidean_distance(a, b):
    return np.sqrt(np.sum(np.square(a - b)))
