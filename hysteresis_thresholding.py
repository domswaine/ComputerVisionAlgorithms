import numpy as np
from morphological_operations import dilate, allDirections


def hysteresis_thresholding(arr, high, low, structure):
    high_thresh = (arr > high).astype(int)
    low_thresh = (arr > low).astype(int)
    return high_thresh + (low_thresh - high_thresh) * dilate(high_thresh, structure)


def main():
    I = np.array([
        [0.4, 0.1, 0.4],
        [0.2, 0.2, 0.7],
        [0.3, 0.8, 0.9]
    ])
    print(hysteresis_thresholding(I, 0.75, 0.25, allDirections))


if __name__ == "__main__":
    main()