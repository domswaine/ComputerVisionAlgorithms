import numpy as np
from math import pi, cos, sin


def deg_to_rad(n: float) -> float:
    return n * pi/180


def hough_transform(arr, angles):
    accumulator = {}
    for x in range(arr.shape[0]):
        for y in range(arr.shape[1]):
            if arr[x][y] == 0:
                for theta in angles:
                    r = x * cos(deg_to_rad(theta)) - y * sin(deg_to_rad(theta))
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


if __name__ == "__main__":
    main()