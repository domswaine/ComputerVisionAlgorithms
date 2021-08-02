import numpy as np
from scipy.ndimage import binary_erosion, binary_dilation
import matplotlib.pyplot as plt

horizontalAndVertical = np.array([
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
])

allDirections = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])


def erode(arr, structure):
    return binary_erosion(arr, structure)


def dilate(arr, structure):
    return binary_dilation(arr, structure)


def close(arr, structure):
    return erode(dilate(arr, structure), structure)


def open(arr, structure):
    return dilate(erode(arr, structure), structure)


def plot(arr):
    arr = np.ones(arr.shape) - arr
    plt.imshow(arr, plt.cm.get_cmap("Greys"))
    plt.show()


def main():
    I = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])

    plot(I)
    plot(dilate(erode(I, horizontalAndVertical), horizontalAndVertical))
    plot(erode(dilate(I, allDirections), allDirections))


if __name__ == "__main__":
    main()