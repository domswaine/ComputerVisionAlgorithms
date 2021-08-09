# python -m unittest edge_directed_interpolation

import numpy as np
import unittest
from numpy import NAN


def edge_directed_interpolation(arr):
    out = np.array(arr).copy()
    x_dim, y_dim = arr.shape
    for x in range(1, x_dim - 1):
        for y in range(1, y_dim - 1):
            if np.isnan(arr[y, x]):
                top = arr[y - 1, x]
                right = arr[y, x + 1]
                bottom = arr[y + 1, x]
                left = arr[y, x - 1]
                horizontal_gradient = np.abs(left - right)
                vertical_gradient = np.abs(top - bottom)
                if horizontal_gradient < vertical_gradient:
                    out[y, x] = 0.5 * (left + right)
                elif horizontal_gradient > vertical_gradient:
                    out[y, x] = 0.5 * (top + bottom)
                else:
                    out[y, x] = 0.25 * (top + bottom + left + right)
    return out


class TestEdgeDirectedInterpolation(unittest.TestCase):
    I = np.array([
        [NAN, 0.3, NAN, 0.3, NAN],
        [0.5, NAN, 0.3, NAN, 0.3],
        [NAN, 0.3, NAN, 0.6, NAN],
        [0.6, NAN, 0.6, NAN, 0.0],
        [NAN, 0.7, NAN, 0.3, NAN]
    ])

    target = np.array([
        [0.3, 0.3, 0.3],
        [0.3, 0.45, 0.6],
        [0.6, 0.6, 0.45],
    ])

    def test_jay_paper(self):
        out = edge_directed_interpolation(self.I)[1:4, 1:4]
        self.assertTrue(np.array_equal(np.around(out, 2), self.target))


def main():
    green_channel = np.array([
        [NAN, 0.3, NAN, 0.3, NAN],
        [0.5, NAN, 0.3, NAN, 0.3],
        [NAN, 0.3, NAN, 0.6, NAN],
        [0.6, NAN, 0.6, NAN, 0.0],
        [NAN, 0.7, NAN, 0.3, NAN]
    ])
    print(np.around(edge_directed_interpolation(green_channel), 3))


if __name__ == "__main__":
    main()
