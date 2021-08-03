import numpy as np
from scipy.signal import convolve2d


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
