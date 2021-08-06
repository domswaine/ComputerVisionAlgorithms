import numpy as np
from numpy import NAN
from offsets import eight_directions as offsets
from bilinear_interpolation import bilinear_interpolation


def smooth_hue_interpolation(primary, green):
    green = bilinear_interpolation(green)
    out = np.array(primary).copy()
    x_dim, y_dim = primary.shape
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


def main():
    green_channel = np.array([
        [NAN, 0.3, NAN, 0.3, NAN],
        [0.5, NAN, 0.3, NAN, 0.3],
        [NAN, 0.3, NAN, 0.6, NAN],
        [0.6, NAN, 0.6, NAN, 0.0],
        [NAN, 0.7, NAN, 0.3, NAN]
    ])

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
