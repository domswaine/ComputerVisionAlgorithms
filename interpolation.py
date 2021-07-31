import numpy as np
from numpy import NAN

offsets = {(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)}


def bilinear_interpolation(arr):
    out = np.array(arr).copy()
    x_dim, y_dim = arr.shape
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


def edge_directed_interpolation(arr):
    out = np.array(arr).copy()
    x_dim, y_dim = arr.shape
    for x in range(1, x_dim - 1):
        for y in range(1, y_dim - 1):
            if np.isnan(arr[y, x]):

    return out


def main():
    red_channel = np.array([
        [NAN, 100, NAN, 100, NAN, 100],
        [NAN, NAN, NAN, NAN, NAN, NAN],
        [NAN, 300, NAN, 300, NAN, 300],
        [NAN, NAN, NAN, NAN, NAN, NAN],
        [NAN, 500, NAN, 500, NAN, 500],
        [NAN, NAN, NAN, NAN, NAN, NAN]
    ])
    green_channel = np.array([
        [100, NAN, 100, NAN, 100, NAN],
        [NAN, 200, NAN, 200, NAN, 200],
        [300, NAN, 300, NAN, 300, NAN],
        [NAN, 400, NAN, 400, NAN, 400],
        [500, NAN, 500, NAN, 500, NAN],
        [NAN, 600, NAN, 600, NAN, 600]
    ])
    blue_channel = np.array([
        [NAN, NAN, NAN, NAN, NAN, NAN],
        [200, NAN, 200, NAN, 200, NAN],
        [NAN, NAN, NAN, NAN, NAN, NAN],
        [400, NAN, 400, NAN, 400, NAN],
        [NAN, NAN, NAN, NAN, NAN, NAN],
        [600, NAN, 600, NAN, 600, NAN]
    ])
    print(np.around(bilinear_interpolation(red_channel)))
    print(np.around(edge_directed_interpolation(red_channel)))


if __name__ == "__main__":
    main()
