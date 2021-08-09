# python -m unittest harris_corner_detector

import numpy as np
import unittest
from scipy.signal import convolve2d

# Notes
# R ≈ 0 -> intensity values are unchanging
# R < 0 -> edges
# R > 0 -> occurs at corners


def harris_corner_detector(Ix, Iy, mask, k=0.05):
    # Compute products of derivatives at every pixel
    Ix2 = Ix * Ix
    Iy2 = Iy * Iy
    Ixy = Ix * Iy

    # Compute sums of the products of derivatives at each pixel
    Sx2 = convolve2d(Ix2, mask, 'same')
    Sy2 = convolve2d(Iy2, mask, 'same')
    Sxy = convolve2d(Ixy, mask, 'same')

    # Compute the response of the detector at each pixel
    determinant = Sx2 * Sy2 - Sxy * Sxy
    trace = Sx2 + Sy2
    return determinant - k * trace * trace


class TestHarrisCornerDetector(unittest.TestCase):
    Ix = np.array([
        [1, 0, 0, 0, 0],
        [-1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    Iy = np.array([
        [1, -1, 0, 0, 0],
        [-1, 0, -1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    mask = np.ones((3, 3))

    target = np.array([
        [3.2, 5.55, 1.55, -0.05, 0],
        [7.8, 12.95, 5.2, 0.55, 0],
        [3.75, 7.8, 3.75, 0.55, 0],
        [-0.2, 1.2, 0.55, -0.2, 0]
    ])

    def test_t6q9(self):
        out = harris_corner_detector(self.Ix, self.Iy, self.mask)
        self.assertTrue(np.array_equal(np.around(out, 2), self.target))


def main():
    Ix = np.array([
        [1, 0, 0, 0, 0],
        [-1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    Iy = np.array([
        [1, -1, 0, 0, 0],
        [-1, 0, -1, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    mask = np.ones((3, 3))

    print(harris_corner_detector(Ix, Iy, mask))


if __name__ == "__main__":
    main()
