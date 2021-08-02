import numpy as np
from morphologicalOperations import dilate, allDirections


def hysteresis_threshold(arr, high, low, structure):
    high_thresh = (arr > high).astype(int)
    low_thresh = (arr > low).astype(int) - high_thresh
    return high_thresh + low_thresh * dilate(arr, structure)


def main():
    I = np.array([
        [0.4, 0.1, 0.4],
        [0.2, 0.2, 0.7],
        [0.3, 0.8, 0.9]
    ])
    print(hysteresis_threshold(I, 0.75, 0.25, allDirections))


if __name__ == "__main__":
    main()