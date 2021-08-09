# python -m unittest smooth_hue_interpolation

import numpy as np
from numpy import NAN
import unittest
from offsets import eight_directions as offsets
from bilinear_interpolation import bilinear_interpolation


def smooth_hue_interpolation(primary, green):
    out = np.array(primary).copy()
    y_dim, x_dim = primary.shape
    for x in range(1, x_dim - 1):
        for y in range(1, y_dim - 1):
            if np.isnan(primary[y, x]):
                ratios = []
                for x_offset, y_offset in offsets:
                    if not np.isnan(primary[y + y_offset, x + x_offset]):
                        primary_intensity = primary[y + y_offset, x + x_offset]
                        green_intensity = green[y + y_offset, x + x_offset]
                        ratios.append(primary_intensity / green_intensity)
                out[y, x] = green[y, x] * (sum(ratios) / len(ratios))
    return out


class TestSmoothHueInterpolation(unittest.TestCase):
    blue = np.array([
        [0.8, NAN, 0.3, NAN, 0.4],
        [NAN, NAN, NAN, NAN, NAN],
        [0.2, NAN, 0.8, NAN, 0.6],
        [NAN, NAN, NAN, NAN, NAN],
        [0.0, NAN, 0.6, NAN, 0.1]
    ])

    green = np.array([
        [0.4, 0.3, 0.3, 0.3, 0.3],
        [0.5, 0.35, 0.3, 0.38, 0.3],
        [0.47, 0.3, 0.45, 0.6, 0.3],
        [0.6, 0.55, 0.6, 0.38, 0.0],
        [0.65, 0.7, 0.53, 0.3, 0.15]
    ])

    target = np.array([
        [0.46, 0.42, 0.58],
        [0.33, 0.8, 1.13],
        [0.46, 0.87, 0.53],
    ])

    def test_jay_paper(self):
        out = smooth_hue_interpolation(self.blue, self.green)[1:4, 1:4]
        self.assertTrue(np.array_equal(np.around(out, 2), self.target))


def main():
    green_channel = bilinear_interpolation(np.array([
        [NAN, 0.3, NAN, 0.3, NAN],
        [0.5, NAN, 0.3, NAN, 0.3],
        [NAN, 0.3, NAN, 0.6, NAN],
        [0.6, NAN, 0.6, NAN, 0.0],
        [NAN, 0.7, NAN, 0.3, NAN]
    ]))

    blue_channel = np.array([
        [NAN, NAN, NAN, NAN, NAN],
        [NAN, 0.3, NAN, 0.0, NAN],
        [NAN, NAN, NAN, NAN, NAN],
        [NAN, 0.4, NAN, 0.3, NAN],
        [NAN, NAN, NAN, NAN, NAN],
    ])

    print(np.around(smooth_hue_interpolation(blue_channel, green_channel), 3), "\n")


if __name__ == "__main__":
    main()
