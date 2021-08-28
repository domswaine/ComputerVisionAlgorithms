# python -m unittest harris_corner_detector

import numpy as np
import unittest


def sum_of_absolute_differences(a, b):
    return np.sum(np.abs(a - b))


def sum_of_squared_differences(a, b):
    return np.sum(np.square(a - b))


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


class TestDistanceMetrics(unittest.TestCase):
    T1 = np.array([
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1],
    ])

    T2 = np.array([
        [1, 0, 0],
        [1, 0, 0],
        [1, 1, 1],
    ])

    T3 = np.array([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ])

    I = np.array([
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1],
    ])

    def test_cross_correlation(self):
        self.assertEqual(cross_correlation(self.T1, self.I), 7)
        self.assertEqual(cross_correlation(self.T2, self.I), 5)
        self.assertEqual(cross_correlation(self.T3, self.I), 7)

    def test_normalised_cross_correlation(self):
        self.assertEqual(round(normalised_cross_correlation(self.T1, self.I), 2), 1)
        self.assertEqual(round(normalised_cross_correlation(self.T2, self.I), 2), 0.85)
        self.assertEqual(round(normalised_cross_correlation(self.T3, self.I), 2), 0.94)

    def test_correlation_coefficient(self):
        self.assertEqual(round(correlation_coefficient(self.T1, self.I), 2), 1)
        self.assertEqual(round(correlation_coefficient(self.T2, self.I), 2), 0.60)
        self.assertEqual(round(correlation_coefficient(self.T3, self.I), 2), 0.66)

    def test_sum_of_absolute_differences(self):
        self.assertEqual(round(sum_of_absolute_differences(self.T1, self.I), 2), 0)
        self.assertEqual(round(sum_of_absolute_differences(self.T2, self.I), 2), 2)
        self.assertEqual(round(sum_of_absolute_differences(self.T3, self.I), 2), 1)

    def test_sum_of_squared_differences(self):
        self.assertEqual(round(sum_of_squared_differences(self.T1, self.I), 2), 0)
        self.assertEqual(round(sum_of_squared_differences(self.T2, self.I), 2), 2)
        self.assertEqual(round(sum_of_squared_differences(self.T3, self.I), 2), 1)

    def test_euclidean_distance(self):
        self.assertEqual(round(euclidean_distance(self.T1, self.I), 2), 0)
        self.assertEqual(round(euclidean_distance(self.T2, self.I), 2), 1.41)
        self.assertEqual(round(euclidean_distance(self.T3, self.I), 2), 1)


if __name__ == "__main__":
    # lista = [np.array([0.3, 0.1, 1.0]), np.array([0.4, 0.4, 1.0]), np.array([0.0, 0.2, 0.0])]
    # listb = [np.array([1.0, 0.5, 0.8]), np.array([0.1, 0.3, 0.2])]
    #
    # for a in lista:
    #     for b in listb:
    #         print(a, b, round(sum_of_absolute_differences(a, b), 4))
    #
    # print("***")
    # a_mean = np.array([0.2333, 0.2333, 0.6667])
    # b_mean = np.array([0.55, 0.4, 0.5])
    # print(a_mean, b_mean, round(sum_of_absolute_differences(a_mean, b_mean), 4))


    # Question 8
    # a = np.array([0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1])
    # b = np.array([0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0])
    # c = np.array([0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1])
    #
    # print(round(cross_correlation(a, b)))
    # print(round(cross_correlation(a, c)))
    # print(round(cross_correlation(b, c)))
    #
    # print(round(correlation_coefficient(a, b)))
    # print(round(correlation_coefficient(a, c)))
    # print(round(correlation_coefficient(b, c)))

    # Question 12
    Q = np.array([4, 4, 1])
    A = np.array([4, 4, 1])
    B = np.array([3, 4, 2])
    C = np.array([2, 3, 4])

    print(euclidean_distance(Q, A))
    print(euclidean_distance(Q, B))
    print(euclidean_distance(Q, C))