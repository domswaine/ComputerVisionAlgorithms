import numpy as np
from numpy import NAN
from offsets import eight_directions as offsets


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
    print(bilinear_interpolation(second_channel))


if __name__ == "__main__":
    main()
