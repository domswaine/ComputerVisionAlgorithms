import numpy as np
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