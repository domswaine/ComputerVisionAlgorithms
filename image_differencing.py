import numpy as np


def image_differencing(series):
    for before, after in zip(series[:-1], series[1:]):
        diff = np.array(before) - np.array(after)
        print(diff)


# Adapt moving average calculation as appropriate
def background_subtraction(series, beta=0.5):
    background = np.zeros(np.array(series[0].shape))
    for image in series:
        background = (1 - beta) * background + beta * image
        diff = np.array(image) - background
        print("Background", background)
        print("Diff", diff)


def main():
    series = [
        np.array([[190, 200, 90, 110, 90]]),
        np.array([[110, 170, 160, 70, 70]]),
        np.array([[100, 60, 170, 200, 90]]),
        np.array([[90, 100, 100, 190, 190]])
    ]
    image_differencing(series)
    background_subtraction(series)


if __name__ == "__main__":
    main()
