# python -m unittest bilinear_interpolation

import numpy as np
from numpy import NAN
import unittest
from offsets import eight_directions as offsets


def bilinear_interpolation(arr):
    out = np.array(arr).copy()
    y_dim, x_dim = arr.shape
    for x in range(x_dim):
        for y in range(y_dim):
            if np.isnan(arr[y, x]):
                intensities = []
                for x_offset, y_offset in offsets:
                    x_pos = x + x_offset
                    y_pos = y + y_offset
                    if 0 <= x_pos < x_dim and 0 <= y_pos < y_dim:
                        value = arr[y_pos, x_pos]
                        if not np.isnan(value):
                            intensities.append(value)
                out[y, x] = sum(intensities) / len(intensities)
    return out


class TestBilinearInterpolation(unittest.TestCase):
    I = np.array([
        [NAN, 0.3, NAN, 0.3, NAN],
        [0.5, NAN, 0.3, NAN, 0.3],
        [NAN, 0.3, NAN, 0.6, NAN],
        [0.6, NAN, 0.6, NAN, 0.0],
        [NAN, 0.7, NAN, 0.3, NAN]
    ])

    target = np.array([
        [0.4, 0.3, 0.3, 0.3, 0.3],
        [0.5, 0.35, 0.3, 0.38, 0.3],
        [0.47, 0.3, 0.45, 0.6, 0.3],
        [0.6, 0.55, 0.6, 0.38, 0.0],
        [0.65, 0.7, 0.53, 0.3, 0.15]
    ])

    def test_jay_paper(self):
        out = bilinear_interpolation(self.I)
        self.assertTrue(np.array_equal(np.around(out, 2), self.target))


def main():
    first_channel = np.array([
        [NAN, 100, NAN, 100, NAN, 100],
        [NAN, NAN, NAN, NAN, NAN, NAN],
        [NAN, 300, NAN, 300, NAN, 300],
        [NAN, NAN, NAN, NAN, NAN, NAN],
        [NAN, 500, NAN, 500, NAN, 500],
        [NAN, NAN, NAN, NAN, NAN, NAN]
    ])
    print(np.around(bilinear_interpolation(first_channel)), "\n")

    second_channel = np.array([
        [0.8, NAN, 0.3, NAN, 0.4],
        [NAN, NAN, NAN, NAN, NAN],
        [0.2, NAN, 0.8, NAN, 0.6],
        [NAN, NAN, NAN, NAN, NAN],
        [0.0, NAN, 0.6, NAN, 0.1]
    ])
    print(bilinear_interpolation(second_channel), "\n")

    third_channel = np.array([
        [NAN, 0.3, NAN, 0.3, NAN],
        [0.5, NAN, 0.3, NAN, 0.3],
        [NAN, 0.3, NAN, 0.6, NAN],
        [0.6, NAN, 0.6, NAN, 0.0],
        [NAN, 0.7, NAN, 0.3, NAN]
    ])
    print(bilinear_interpolation(third_channel))


if __name__ == "__main__":
    main()
