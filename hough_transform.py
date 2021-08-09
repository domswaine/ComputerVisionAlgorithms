# python -m unittest hough_transform

import numpy as np
import unittest
from math import cos, sin, radians


def hough_transform(arr, angles):
    accumulator = {}
    y_dim, x_dim = arr.shape
    for x in range(x_dim):
        for y in range(y_dim):
            if arr[y, x] == 0:
                for theta in angles:
                    r = round(y * cos(radians(theta)) - x * sin(radians(theta)), 3)
                    key = (theta, round(r))
                    if key not in accumulator:
                        accumulator[key] = 0
                    accumulator[key] += 1
    return accumulator


class TestHoughTransform(unittest.TestCase):
    I = np.array([
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 1]
    ])

    def test_t5q18(self):
        target = {
            (0, 2): 1, (0, 1): 1, (0, 0): 2,
            (45, 0): 3, (45, -2): 1,
            (90, 0): 1, (90, -1): 1, (90, -2): 1, (90, -3): 1,
            (135, 0): 1, (135, -1): 1, (135, -2): 1, (135, -3): 1
        }
        self.assertEqual(hough_transform(self.I, [0, 45, 90, 135]), target)

    def test_t5q19(self):
        target = {
            (0, 2): 1, (0, 1): 1, (0, 0): 2,
            (30, 1): 1, (30, 0): 2, (30, -2): 1,
            (60, 0): 2, (60, -1): 1, (60, -3): 1,
            (90, 0): 1, (90, -1): 1, (90, -2): 1, (90, -3): 1,
            (120, 0): 1, (120, -1): 1, (120, -3): 2,
            (150, 0): 1, (150, -1): 1, (150, -2): 1, (150, -3): 1
        }
        self.assertEqual(hough_transform(self.I, [0, 30, 60, 90, 120, 150]), target)


def main():
    I = np.array([
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 1]
    ])
    print(hough_transform(I, [0, 45, 90, 135]))
    print(hough_transform(I, [0, 30, 60, 90, 120, 150]))


if __name__ == "__main__":
    main()
